from tyre import Tyre

class Lap:
        def __init__(self, lap_average,tyre,):
                self.lap_average = lap_average
                self.tyre = tyre
                self.lap_time = None

        
        def lap_performance(self, number_of_laps, percurso):
                (tyre_wear,tyre_speed) = self.tyre.tyre_performance(number_of_laps, percurso)
                self.lap_time = self.lap_average + self.lap_average*(tyre_wear+tyre_speed)
                return self.lap_time, tyre_wear*5