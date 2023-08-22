from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from controller.exercise import ExerciseController
from controller.user import UserController
from model.exercise import Exercises

app = Flask(__name__)
CORS(app)


@app.route('/login', methods=['POST'])
def login():
    user_controller = UserController()

    email = request.json.get('email')

    # hashPassword = bcrypt.generate_password_hash('password').decode('utf-8')

    # print(hashPassword)

    return 'oi'


@app.route('/list-all', methods=['GET'])
def get_all_exercises():
    exController = ExerciseController()

    data = exController.get_all_exercises()

    return make_response(data['data'], data['status'])


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
    exController = ExerciseController()

    data = exController.remove_exercise(exercise_id)

    return make_response(jsonify(data), data['status'])
