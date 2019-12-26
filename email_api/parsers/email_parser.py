from __future__ import annotations
from abc import ABC, abstractmethod
import mailparser
from email.parser import Parser
from email import message_from_string

class EmailParser(ABC):

    def __init__(self):
        self.to = ""
        self.from_ = ""
        self.date = ""
        self.subject = ""
        self.message_id = ""
        super().__init__()

    @abstractmethod
    def parse_from_string(self, message):
        pass


class PythonEmailParser(EmailParser):

    def parse_from_string(self, email_message):
        parser = Parser()
        msg = parser.parsestr(email_message)
        print(msg)
        self.to = msg['to']
        self.from_ = msg['from']
        self.date = msg['date']
        self.subject = msg['subject']
        self.message_id = msg['message-id']


class MailParserEmailParser(EmailParser):
    
    def __init__(self):
        super().__init__()
        self.mailparser = None

    def parse_from_string(self, message):
        self.mailparser = mailparser.parse_from_string(message)
        if self.mailparser.to:
            self.to = self.mailparser.to
        if self.mailparser.from_:
            self.from_ = self.mailparser.from_
        if self.mailparser.date_raw:
            self.date = self.mailparser.date_raw.replace('[','').replace(']','').replace('"','')
        if self.mailparser.subject:
            self.subject = self.mailparser.subject
        if self.mailparser.message_id:
            self.message_id = self.mailparser.message_id
    
class EmailParseStrategy(object):

    def __init__(self, parser: EmailParser):
        self.mailparser = parser

    @property
    def emailParser(self) -> EmailParser:
        return self.mailparser

    @emailParser.setter
    def setParser(self, parser: EmailParser):
        self.mailparser = parser

    def parse_email_from_string(self, message):
        return self.mailparser.parse_from_string(message)
