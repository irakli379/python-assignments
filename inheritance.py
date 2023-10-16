class Person:
    def __init__(self, name, surname, age):
        self.surname = surname
        self.name = name
        self.age = age



class Student(Person):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, surname: {self.surname}, University: {self.university}."
