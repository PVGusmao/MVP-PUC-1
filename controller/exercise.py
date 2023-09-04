from model.exercise import Exercises
from model import Session


class ExerciseController():
    def get_all_exercises(self, user_id):
        session = Session()

        try:
            data = session.query(Exercises).filter_by(user_id=user_id)

            array_exercises = []

            for exercise in data:
                lib = {
                    "day_serie": exercise.day_serie,
                    "name": exercise.name,
                    "video_exercise": exercise.video_exercise,
                    "muscle_group": exercise.muscle_group,
                    "series": exercise.series,
                    "series_repeats": exercise.series_repeats,
                    "identify": exercise.identify,
                    "user_id": exercise.user_id
                }

                array_exercises.append(lib)

            return {
                "status": 200,
                "message": "Produto listado",
                "data": array_exercises,
            }

        except Exception as e:
            error_msg = "Algo deu errado, tente novamente."
            return {
                "status": 400,
                "message": error_msg,
            }

    def get_last_serie(self, user_id):
        session = Session()

        try:
            # data = session.query(Exercises).all()
            data = session.query(Exercises).filter_by(user_id=user_id)
            largest_identify = 0

            for exercise in data:
                print(exercise)
                if largest_identify < exercise.identify:
                    largest_identify = exercise.identify

            return {
                "status": 200,
                "message": "Identificador da última série criada.",
                "data": largest_identify,
            }

        except Exception as e:
            error_msg = "Algo deu errado, tente novamente."
            return {
                "status": 400,
                "message": error_msg,
            }

    def remove_exercise(self, exercise_id):
        session = Session()

        count = session.query(Exercises).filter(
            Exercises.id == exercise_id).delete()

        session.commit()

        if count == 1:
            return {
                "status": 200,
                "message": "Producto excluído com sucesso."
            }
        else:
            error_msg = "Produto não encontrado."
            return {
                "status": 404,
                "message": error_msg
            }

    def add_exercise(self, exercise):
        session = Session()
        data = session.query(Exercises).all()

        # for each_element in data:
        #     if each_element.name == exercise.name:
        #         return {
        #             "status": 409,
        #             "message": "Já exsite um cadastro com este nome.",
        #         }

        json_exercise = exercise.jsonified_exercise()

        try:
            session.add(exercise)
            session.commit()
            return {
                "status": 200,
                "exercise": json_exercise
            }

        except Exception as e:
            error_msg = "Não foi possível salvar novo item :/"
            print(str(e))
            return {
                "status": 400,
                "exercise": json_exercise,
                "message": error_msg,
            }
