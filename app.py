from flask import Flask, request, jsonify, make_response

from controller.exercise import ExerciseController

from model import Session
from model.exercise import Exercises

app = Flask(__name__)


@app.route('/list-all', methods=['GET'])
def get_all_exercises():
    session = Session()

    try:
        data = session.query(Exercises).all()

        array_exercises = []

        for exercise in data:
            lib = {
                "day_serie": exercise.day_serie,
                "name": exercise.name,
                "muscle_group": exercise.muscle_group,
                "series": exercise.series,
                "series_repeats": exercise.series_repeats,
            }

            array_exercises.append(lib)

        return make_response(jsonify(array_exercises), 200)
    except Exception as e:
        error_msg = "Algo deu errado, tente novamente."
        return make_response(jsonify({
            "message": error_msg,
        }), 400)


# @app.route('/add-exercise', methods=['POST'])
# def add_exercise():
#     session = Session()
#     exercise = Exercises(
#         day_serie=request.json.get("day_serie"),
#         name=request.json.get("name"),
#         muscle_group=request.json.get("muscle_group"),
#         series=request.json.get("series"),
#         series_repeats=request.json.get("series_repeats"),
#     )

#     data = session.query(Exercises).all()

#     for each_element in data:
#         if each_element.name == exercise.name:
#             return make_response(jsonify({
#                 "message": "Já exsite um cadastro com este nome.",
#             }), 409)

#     json_exercise = exercise.jsonified_exercise()

#     try:
#         session.add(exercise)
#         session.commit()
#         return make_response(jsonify({
#             "exercise": json_exercise
#         }), 200)

#     except Exception as e:
#         error_msg = "Não foi possível salvar novo item :/"
#         print(str(e))
#         return make_response(jsonify({
#             "exercise": exercise,
#             "message": error_msg,
#         }), 400)


@app.route('/add-exercise', methods=['POST'])
def add_exercise():
    exercise = Exercises(
        day_serie=request.json.get("day_serie"),
        name=request.json.get("name"),
        muscle_group=request.json.get("muscle_group"),
        series=request.json.get("series"),
        series_repeats=request.json.get("series_repeats"),
    )

    exercise_controller = ExerciseController()

    new_data = exercise_controller.add_exercise(exercise)

    return make_response(jsonify(new_data), new_data['status'])

@app.route('/remove-exercise/<exercise_id>', methods=['DELETE'])
def remove_exercise(exercise_id):
    session = Session()
    count = session.query(Exercises).filter(
        Exercises.id == exercise_id).delete()
    session.commit()
    if count == 1:
        return make_response(jsonify({
            "message": "Producto excluído com sucesso."
        }), 200)
    else:
        error_msg = "Produto não encontrado."
        return make_response(jsonify({
            "message": error_msg
        }), 404)
