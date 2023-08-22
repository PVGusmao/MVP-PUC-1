from model.exercise import Exercises
from model import Session

class ExerciseController():
    def add_exercise(self, exercise):
        session = Session()
        data = session.query(Exercises).all()

        for each_element in data:
            if each_element.name == exercise.name:
                return {
                    "status": 409,
                    "message": "Já exsite um cadastro com este nome.",
                }
        
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
                "exercise": exercise,
                "message": error_msg,
            }
