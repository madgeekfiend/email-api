from flask import Flask
from .api.controllers_v1 import api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = './uploads'
app.register_blueprint(api, url_prefix='/api/v1')