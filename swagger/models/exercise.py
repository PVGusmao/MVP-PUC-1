from flask_restx import fields

from swagger.api.instance import server

nested_keys = server.api.model('Base', {
  "muscle_group": fields.String(required=True, description='Nome do grupo muscular a ser treinado.'),
  "name": fields.String(required=True, description='Nome do exercício.'),
  "series": fields.String(required=True, description='Quantidade de séries do exercício'),
  "series_repeats": fields.String(required=True, description='Número de repetições por série do exercício.'),
})

exercise_register = server.api.model('Exercise', {
  'day_serie': fields.String(required=True, description='O dia da série (A, B, C, D ou E)'), 
  "identify": fields.Integer(required=True, description='Identificador da série'),
  'exercise': fields.Wildcard(fields.Nested(nested_keys)),
})
