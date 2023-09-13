from flask_jwt_extended import create_access_token

from model.user import User
from model import Session


class UserController():
    session = Session()

    def login(self, email, password, bcrypt):
        data = self.session.query(User).filter_by(email=email).first()

        if data == None:
            return {
                "status": 404,
                "message": "E-mail or password invalid, please try again with different credentials."
            }

        json_data = User.jsonified_exercise(data)

        confirm_password = bcrypt.check_password_hash(
            json_data['password'], password)

        if confirm_password == False:
            return {
                "status": 400,
                "message": "E-mail or password invalid, please try again with different credentials."
            }

        token = create_access_token(json_data)

        return {
            "status": 200,
            "message": "User logged in successfully.",
            "token": token,
            "user": json_data
        }

    def register_user(self, user):
        json_user = user.jsonified_exercise()
        print(json_user)

        try:
            self.session.add(user)
            self.session.commit()
            return {
                "status": 200,
                "user": json_user
            }

        except Exception as e:
            error_msg = "Não foi possível salvar novo item :/"
            print(str(e))
            self.session.rollback()
            return {
                "status": 400,
                "user": json_user,
                "message": error_msg,
            }
