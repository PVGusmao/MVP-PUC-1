from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from flask_restx import Api

from flask_jwt_extended import jwt_required, JWTManager, get_jwt_identity

from controller.exercise import ExerciseController
from controller.user import UserController
from model.exercise import Exercises
from model.user import User

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)

api = Api(app,
            title="Example API application",
            description="An example API application using flask-restx",
            version="1.0",
            doc="/swagger/",
            validate=True)


@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    user_controller = UserController()

    data = user_controller.login(email, password, bcrypt)

    return make_response(jsonify(data), data['status'])


@app.route('/register-user', methods=['POST'])
def register_user():
    user = User(
        first_name=request.json.get("first_name"),
        last_name=request.json.get("last_name"),
        cpf=request.json.get("cpf"),
        birth_date=request.json.get("birth_date"),
        email=request.json.get("email"),
        password=bcrypt.generate_password_hash(
            request.json.get('password')).decode('utf-8')
    )

    user_controller = UserController()

    data = user_controller.register_user(user)

    return data


@app.route('/exercise/list', methods=['GET'])
@jwt_required()
def get_all_exercises():
    user = get_jwt_identity()
    user_id = user["id"]

    exController = ExerciseController()

    data = exController.get_all_exercises(user_id)

    return make_response(jsonify(data), data['status'])


@app.route('/exercise/lastserie', methods=['GET'])
@jwt_required()
def get_last_serie():
    user = get_jwt_identity()
    user_id = user["id"]

    exController = ExerciseController()

    data = exController.get_last_serie(user_id)

    return make_response(jsonify(data), data['status'])


@app.route('/exercise/add', methods=['POST'])
@jwt_required()
def add_exercise():
    user = get_jwt_identity()

    day_serie = request.json.get("day_serie")
    identify = request.json.get("identify")
    exercises = request.json.get("exercises")

    new_data = 0

    for each in exercises:
        exercise = Exercises(
            day_serie=day_serie,
            name=each["name"],
            muscle_group=each["muscle_group"],
            video_exercise=None,
            series=each["series"],
            series_repeats=each["series_repeats"],
            identify=identify,
            user_id=user['id'],
        )

        exercise_controller = ExerciseController()

        new_data = exercise_controller.add_exercise(exercise)

        if new_data['status'] != 200:
            break

    return make_response(jsonify(new_data), new_data["status"])


@app.route('/exercise/remove/<exercise_id>', methods=['DELETE'])
@jwt_required()
def remove_exercise(exercise_id):
    exController = ExerciseController()

    data = exController.remove_exercise(exercise_id)

    return make_response(jsonify(data), data['status'])
