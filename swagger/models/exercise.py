from flask_restx import fields

from swagger.api.instance import server

exercise_register = server.api.model('Exercise', {
  'day_serie': fields.String(required=True, description='O dia da série (A, B, C, D ou E)'), 
  "identify": fields.String(required=True, description='Identificador da série'),
  "exercises": fields.List(fields.String(), required=True, default=[{
    "muscle_group": fields.String(required=True, description='Nome do grupo muscular a ser treinado.'),
    "name": fields.String(required=True, description='Nome do exercício.'),
    "series": fields.String(required=True, description='Quantidade de séries do exercício'),
    "series_repeats": fields.String(required=True, description='Número de repetições por série do exercício.'),
  }])
})
