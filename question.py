class Option():
    def __init__(self, name) -> None:
        self.name = name
        self.isCorrect = False

class Question():
    def __init__(self, name, option1=None, option2=None, option3=None, option4=None, option5=None, option6=None, exam_id=None) -> None:
        self.name = name
        self.question_id = exam_id
        self.options = [
            Option(option1),
            Option(option2),
            Option(option3),
            Option(option4),
            Option(option5),
            Option(option6)
        ]