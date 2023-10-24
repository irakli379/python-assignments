class Person:
    def __init__(self):
        self.heart = None
        self.brain = None



class Heart:
    def __init__(self, usage):
        self.usage = usage

    
    def state(self):
        if self.usage > 70:
            return 'high blood pressure'
        else:
            return 'feeling good'


class Brain:
    def __init__(self, usage):
        self.usage = usage


    def state(self):
        if self.usage > 90:
            return 'tired'
        else:
            return 'rested'


class Leg:
    def __init__(self, moving_speed, state='k'):
        self.moving_speed = moving_speed
        self.state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, val):
        if self.moving_speed > 10:
            self._state = 'running'
        else:
            self._state = 'walking'
            
  
