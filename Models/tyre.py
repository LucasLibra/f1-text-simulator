import random

class Tyre:
    def __init__(self, tyre_speed,tyre_name):
        self.tyre_name = tyre_name
        self.tyre_speed = tyre_speed

    def tyre_performance(self, number_of_laps, percurso):
        if self.tyre_name == "Soft":
            tyre_wear = number_of_laps*percurso/58480
        elif self.tyre_name == "Medium":
            tyre_wear = number_of_laps*percurso/73100
        elif self.tyre_name == "Hard":
            tyre_wear = number_of_laps*percurso/93568
          
        tyre_wear_aux = random.uniform(0,tyre_wear)/5
        tyre_speed_aux = random.uniform(self.tyre_speed-0.01,self.tyre_speed)
        return tyre_wear_aux, tyre_speed_aux

    def getName(self):
        return self.tyre_name