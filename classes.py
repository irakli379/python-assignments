class Student:

    university = 'TSU'
    
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
        self.is_passing = self.grade > 60


    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}."


    def increase_grade(self, num):
        self.grade = self.grade + num
