from flask_restx import fields

from swagger.api.instance import server

user = server.api.model('User', {
  'email': fields.String(required=True, description='O e-mail do usuário.'),
  'password': fields.String(required=True, min_length=3, max_length=20, description="O password do usuário.")
})