from abc import ABC, abstractmethod


class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass


    @abstractmethod
    def stop_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, max_speed, current_speed):
        self.max_speed = max_speed
        self.current_speed = current_speed


    def start_engine(self):
        return 'car started'


    def stop_engine(self):
        return 'car stopped'


class SportCar(Car):
    def __init__(self, max_speed, current_speed):
        super().__init__(max_speed, current_speed)


    def start_engine(self):
        return f'car started {self.max_speed}'


    def stop_engine(self):
        self.current_speed = 0
        return f'car stopped, speed is {self.current_speed}'

