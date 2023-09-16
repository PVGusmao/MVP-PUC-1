from flask import Flask
from flask_restx import Api

class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            title="Swagger API MVP Puc",
            description="Designed to perform all the requests from mvp api - Gym Bro",
            version="1.0",
            doc="/docs",
            validate=True,
            security='apikey',
            authorizations = {
                'apikey': {
                    'type': 'apiKey',
                    'in': 'header',
                    'name': 'Authorization',
                    'description': "Adicione o valor do token jwt no input abaixo."
                }
            }
        )
    
    def run (self, ):
        self.app.run(
            debug=true
        )

server = Server()