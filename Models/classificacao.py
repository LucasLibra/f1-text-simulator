from lap import Lap
from tyre import Tyre
from circuito import Circuit
import datetime
import pandas as pd

class Qualifying:
        def __init__(self, circuit, drivers):
                self.circuit = circuit
                self.drivers = drivers

        def classificacao(self):
            #number_of_laps = self.circuit.getNumberOfLaps()
            percurso = self.circuit.getPercurso()
            lap_average = self.circuit.getLapAverage()
            laps = []
            for i in range(0,len(self.drivers)):
                tyre_age = self.drivers[i].getTyreAge()
                max = 0
                for j in range(0,3):
                    lap = Lap(lap_average = lap_average, tyre = self.drivers[i].getTyreCompound())
                    lap_qualy = lap.lap_performance(number_of_laps = tyre_age, percurso = percurso)
                    if lap_qualy >= max:
                        max = lap_qualy
                    tyre_age += 1
                best_lap_time = str(datetime.timedelta(seconds=max))
                data = {
                    'Name':self.drivers[i].getName(),
                    'Nationality': self.drivers[i].getNationality(),
                    'Team':self.drivers[i].getTeam(),
                    'Number':self.drivers[i].getNumber(),
                    'Tyre_Compound':self.drivers[i].getTyreCompound().getName(),
                    'Lap_Time':best_lap_time
                }
                laps.append(data)
            df = pd.DataFrame(laps)
            df_sorted = df.sort_values(by='Lap_Time', ascending=True)
            print(df_sorted)
            df_sorted.to_excel('classificacao.xlsx', index=False)                   
            