from model.user import User
from model import Session


class UserController():
    session = Session()

    def __init__(self,):
        pass
        # hashPassword = bcrypt.generate_password_hash(password).decode('utf-8')
        # print(hashPassword, bcrypt.check_password_hash(hashPassword, '#Paulo2010.'))

    # def login(self, ):
    #     data = self.session.query(User).filter_by(email=self._email)
    #     print(data)

    def register_user(self, user):
        # data = self.session.query(User).filter_by(email=user.email).first()

        json_user = user.jsonified_exercise()

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
            return {
                "status": 400,
                "user": json_user,
                "message": error_msg,
            }