class Student:

    def __init__(self, name , roll, gpa) -> None:
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def on_regular(self) :
        if self.gpa > 6:
            return True
        else :
            return False