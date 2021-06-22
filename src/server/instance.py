from flask import Flask
from flask_restplus import Api


class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='time',
            description='time',
            doc='/docs'
        )

    def run(self):
        self.app.run(
            host='localhost', port=5000,
            debug=True
        )

server = Server()