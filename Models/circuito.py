class Circuit:
        def __init__(self, name, lap_average,number_of_laps,percurso):
                self.name = name
                self.lap_average = lap_average
                self.number_of_laps = number_of_laps
                self.percurso = percurso
        
        def getName(self):
            return self.name
        
        def getNumberOfLaps(self):
            return self.number_of_laps

        def getLapAverage(self):
            return self.lap_average

        def getPercurso(self):
            return self.percurso