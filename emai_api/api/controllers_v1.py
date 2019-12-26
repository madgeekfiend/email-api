from flask import Blueprint, request, abort, current_app as app
from http import HTTPStatus
import mailparser
from ..parsers.email_parser import EmailParseStrategy, MailParserEmailParser, PythonEmailParser
import docx
import os
from werkzeug.utils import secure_filename
from flask_cors import cross_origin

api = Blueprint('api', __name__)

def __getTextFromDocxFile(filename):
    doc = docx.Document(filename)
    fullText = []
    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
    return '\n'.join(fullText)

@api.route('/health')
def health_check():
    return ({"status":"ok"}, HTTPStatus.OK)

@api.route('/email/parse', methods=['POST'])
@cross_origin()
def parse_email():
    # Handle CORS just allow it for all domains
    # In production would lock it down more

    if request.method == 'POST':
        message = None
        app.logger.info("Receiving call to email parse")
        request_data = request.get_json()
        if request_data: # sent a JSON payoad in the body
            app.logger.debug("email parse JSON body present")
            app.logger.debug(request_data)
            message = request_data['emailRawText']
        # elif request.form['emailRawText'] != "":
        #     app.logger.debug("email form data present")
        #     message = request.form["emailRawText"]
        #     app.logger.debug(message)
        elif request.files['emailFile'] != "":
            emailMessage = request.files['emailFile']
            emailMessage.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(emailMessage.filename)))
            # Now process this file that was just saved
            # goto beginning of file https://stackoverflow.com/questions/28438141/python-flask-upload-file-but-do-not-save-and-use/46658399
            emailMessage.stream.seek(0)
            fileExtension = emailMessage.filenamer.split('.', 1)[1].lower()
            if fileExtension == 'docx':
                message = __getTextFromDocxFile(emailMessage)
            elif fileExtension == 'txt':
                message = emailMessage.read()
                print(message)
        if message == None: # No message present
            abort(HTTPStatus.BAD_REQUEST)
        emailParseStrategy = EmailParseStrategy(MailParserEmailParser())
        emailParseStrategy.parse_email_from_string(message)

        return {
            "to": emailParseStrategy.emailParser.to,
            "from": emailParseStrategy.emailParser.from_,
            "date": emailParseStrategy.emailParser.date,
            "subject": emailParseStrategy.emailParser.subject,
            "messageId": emailParseStrategy.emailParser.message_id
        }
