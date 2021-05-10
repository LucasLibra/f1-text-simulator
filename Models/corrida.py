from lap import Lap
from tyre import Tyre
from circuito import Circuit
import pandas as pd
import datetime
import random
import math 

class Race:
        def __init__(self, circuit, drivers, tyres):
                self.circuit = circuit
                self.drivers = drivers
                self.df_qualy = pd.read_excel("classificacao.xlsx")
                self.tyres = tyres
        
        def race(self):
                percurso = self.circuit.getPercurso()
                lap_average = self.circuit.getLapAverage()
                number_of_laps = self.circuit.getNumberOfLaps()
                max = 100
                min = 100
                piloto_volta_mais_rapida = ''
                for j in range(0,number_of_laps):
                        min = 50000
                        positions = []
                        # pit_stop = input("Alguém quer fazer pitstop?: ")
                        # while pit_stop == 'Sim':
                        #         piloto = input("Qual o nome do piloto?: ")
                        #         for i in range(0,len(self.drivers)):
                        #                 if piloto == self.drivers[i].getName():
                        #                         tyre = input("Para qual componente de pneus?: ")
                        #                         for n in range(0,len(self.tyres)):
                        #                                 if self.tyres[n].getName() == tyre:
                        #                                         tyre = self.tyres[n]
                        #                         self.drivers[i].setTyreCompound(tyre)
                        #                         self.drivers[i].setTyreAge(0)
                        #                         self.drivers[i].setHasDonePit(True)
                        #         pit_stop = input("Deseja continuar?: ")

                        for i in range(0,len(self.drivers)):
                                lap_race = 0
                                
                                tyre_age = self.drivers[i].getTyreAge()
                                lap = Lap(lap_average = lap_average, tyre = self.drivers[i].getTyreCompound())
                                lap_race_aux, tyre_wear = lap.lap_performance(number_of_laps = tyre_age, percurso = percurso)
                                lap_race += lap_race_aux



                                if j == 0:
                                        for index, row in self.df_qualy.iterrows():
                                                name = row['Name']
                                                if name == self.drivers[i].getName():
                                                        lap_race +=  index*0.75
                                                        
                                if lap_race < max:
                                        max = lap_race
                                        piloto_volta_mais_rapida = self.drivers[i].getName()
                                
                                e_tyre_wear = math.exp(4.7*tyre_wear-2.5) - 0.4
                                pit_chance = random.uniform(0,e_tyre_wear)

                                if pit_chance > 0.65:
                                        self.drivers[i].setHasDonePit(True)

                                if self.drivers[i].getHasDonePit() == True:
                                        pit_time = random.uniform(1.9,4)
                                        print("O pitstop de %s foi de %f s" % (self.drivers[i].getName(),pit_time))
                                        lap_race += pit_time + random.uniform(25,27)
                                        tyre = random.choice(self.tyres)
                                        self.drivers[i].setTyreAge(0)
                                        self.drivers[i].setTyreCompound(tyre)
                                        self.drivers[i].setHasDonePit(False)

                                tyre_age = self.drivers[i].getTyreAge()
                                race_time = self.drivers[i].getRaceTime() + lap_race
                                self.drivers[i].setRaceTime(race_time)
                                race_time_timedelta = str(datetime.timedelta(seconds=race_time))
                                lap_race_timedelta = str(datetime.timedelta(seconds=lap_race))
                                self.drivers[i].setTyreAge(tyre_age+1)

                                if race_time <= min:
                                        min = race_time

                                gap_to_leader = race_time - min
                               
                                gap_to_leader = '+' + str(datetime.timedelta(seconds=gap_to_leader))
                                data = {
                                        'Name':self.drivers[i].getName(),
                                        'Nationality': self.drivers[i].getNationality(),
                                        'Number':self.drivers[i].getNumber(),
                                        'Team':self.drivers[i].getTeam(),
                                        'Tyre_Compound':self.drivers[i].getTyreCompound().getName(),
                                        'Race_Time':race_time_timedelta,
                                        'Lap_Time':lap_race_timedelta,
                                        'Tyre_Age': tyre_age+1,
                                        'Gap_To_Leader':gap_to_leader
                                        }
                                positions.append(data)
                        df = pd.DataFrame(positions)
                        df_sorted = df.sort_values(by='Race_Time', ascending=True)
                        print("Lap: %i/%i" % (j,number_of_laps))
                        print(df_sorted)
                        print("Volta mais rápida: %s - %s" % (str(datetime.timedelta(seconds=max)), piloto_volta_mais_rapida))
                        input("Press Enter to continue...")
                df_sorted.to_excel('classificacao_final.xlsx', index=False)        
