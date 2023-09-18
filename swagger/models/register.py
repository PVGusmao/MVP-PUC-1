from flask_restx import fields

from swagger.api.instance import server

register = server.api.model('User', {
  'first_name': fields.String(required=True, description='O primeiro nome do usuário.'), 
  "last_name": fields.String(required=True, description='O segundo nome do usuário.'),
  "cpf": fields.String(required=True, min_length=11, max_length=11, description='O cpf do usuário.'),
  "birth_date": fields.String(required=True, description='A data de nascimento do usuário.(por favor inserir as barras "/")'),
  'email': fields.String(required=True, description='O e-mail do usuário.'),
  'password': fields.String(required=True, min_length=3, max_length=20, description="O password do usuário.")
})
