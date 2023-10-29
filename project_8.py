from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def display_details(self):
        pass


class Student(Person):
    def __init__(self, name, student_id, grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grade):
        self._grades = grade

    def add_grade(self, grade):
        if type(self.grades) == int or type(self.grades) == float:
            self.grades = [self.grades]
            return self.grades.append(grade)
        elif type(self.grades) == list:
            return self.grades.append(grade)
        else:
            return 'Wrong variable type'

    def avarage_grade(self):
        if type(self.grades) == int or type(self.grades) == float:
            return round(self.grades)
        else:
            n = sum(self.grades) / len(self.grades)
            return round(n)

    def display_details(self):
        return f"Student name: {self.name}, id: {self.student_id}, average grade: {self.avarage_grade()}"


class StudentManagementSystem:
    
    def add_student(self):
        pass

    def show_student_details(self):
        pass

    def show_student_avarage_grade(self):
        pass

