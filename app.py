from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_bcrypt import Bcrypt

from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

from controller.exercise import ExerciseController
from controller.user import UserController
from model.exercise import Exercises
from model.user import User

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    hash_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    user_controller = UserController(email, hash_password)

    user_controller.login()

    return 'User Login'

@app.route('/register-user', methods=['POST'])
def register_user():
    user = User(
        first_name = request.json.get("first_name"),
        last_name = request.json.get("last_name"),
        cpf = request.json.get("cpf"),
        birth_date = request.json.get("birth_date"),
        email = request.json.get("email"),
        password = bcrypt.generate_password_hash(request.json.get('password')).decode('utf-8')
    )

    user_controller = UserController()

    data = user_controller.register_user(user)

    return data


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
