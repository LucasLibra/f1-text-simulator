from lap import Lap
from tyre import Tyre
from circuito import Circuit
import pandas as pd
import datetime
import random
import math 
import time

class Race:
        def __init__(self, circuit, drivers, tyres):
                self.circuit = circuit
                self.drivers = drivers
                self.df_qualy = pd.read_excel("classificacao.xlsx", index_col=None)
                self.tyres = tyres
        
        def race(self):
                percurso = self.circuit.getPercurso()
                lap_average = self.circuit.getLapAverage()
                number_of_laps = self.circuit.getNumberOfLaps()
                max = 100
                prob = 0.15/number_of_laps
                piloto_volta_mais_rapida = ''
                dnf = []
                number_of_laps_safety_car = 0

                for j in range(1,number_of_laps+1):

                        positions = []
                        min = 7000000

                        for driver in self.drivers:
                                if driver.getIsOut() == True:
                                        self.drivers.pop(self.drivers.index(driver))

                        for driver in self.drivers:
                                if driver.getRaceTime() < min:
                                        min = driver.getRaceTime()             

                        race_time_leader = min
                        if self.circuit.getIsSCOut() == False:
                                for i in range(0,len(self.drivers)):
                                        damage = random.uniform(0,1)
                                        if damage > prob:
                                                lap_race = 0
                                                
                                                tyre_age = self.drivers[i].getTyreAge()
                                                lap = Lap(lap_average = lap_average, tyre = self.drivers[i].getTyreCompound())
                                                lap_race_aux, tyre_wear = lap.lap_performance(number_of_laps = tyre_age, percurso = percurso)
                                                lap_race += lap_race_aux


                                                if j == 1:
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
                                                        if (number_of_laps - j) > number_of_laps*0.15:
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

                                        
                                                data = {
                                                        'Name':self.drivers[i].getName(),
                                                        'Nationality': self.drivers[i].getNationality(),
                                                        'Number':self.drivers[i].getNumber(),
                                                        'Team':self.drivers[i].getTeam(),
                                                        'Tyre_Compound':self.drivers[i].getTyreCompound().getName(),
                                                        'Race_Time':race_time_timedelta,
                                                        'Lap_Time':lap_race_timedelta,
                                                        'Tyre_Age': tyre_age+1,

                                                        }
                                                positions.append(data)
                                        else:
                                                print("%s is out of this Grand Prix" % self.drivers[i].getName())
                                                data = {
                                                        'Name':self.drivers[i].getName(),
                                                        'Nationality': self.drivers[i].getNationality(),
                                                        'Number':self.drivers[i].getNumber(),
                                                        'Team':self.drivers[i].getTeam(),
                                                        'Tyre_Compound':'DNF',
                                                        'Race_Time':'DNF',
                                                        'Lap_Time':'DNF',
                                                        'Tyre_Age': 'DNF',
                                                        }
                                                self.drivers[i].setIsOut(True)
                                                self.circuit.setIsSCOut(True)
                                                dnf.append(data)
                                                number_of_laps_safety_car = 0
                        else:
                                for i in range(0,len(self.drivers)):
                                        tyre_age = self.drivers[i].getTyreAge()

                                        lap_race = lap_average + 30
                                        _, tyre_wear = lap.lap_performance(number_of_laps = tyre_age, percurso = percurso)
                                        e_tyre_wear = math.exp(4.7*tyre_wear-2.5) - 0.2
                                        pit_chance = random.uniform(0,e_tyre_wear)

                                        if pit_chance > 0.20:
                                                if (number_of_laps - j) > number_of_laps*0.15:
                                                        self.drivers[i].setHasDonePit(True)

                                        if self.drivers[i].getHasDonePit() == True:
                                                pit_time = random.uniform(1.9,4)
                                                print("O pitstop de %s foi de %f s" % (self.drivers[i].getName(),pit_time))
                                                lap_race += pit_time + random.uniform(25,27)
                                                tyre = random.choice(self.tyres)
                                                self.drivers[i].setTyreAge(0)
                                                self.drivers[i].setTyreCompound(tyre)
                                                self.drivers[i].setHasDonePit(False)

                                        race_time = min + lap_race
                                                
                                        for index, row in df_sorted.iterrows():
                                                name = row['Name']
                                                if name == self.drivers[i].getName():
                                                        race_time +=  index*0.75

                                        tyre_age = self.drivers[i].getTyreAge()
                                        self.drivers[i].setRaceTime(race_time)
                                        race_time_timedelta = str(datetime.timedelta(seconds=race_time))
                                        lap_race_timedelta = str(datetime.timedelta(seconds=lap_race))
                                        self.drivers[i].setTyreAge(tyre_age+1)
                                        
                                        data = {
                                                                'Name':self.drivers[i].getName(),
                                                                'Nationality': self.drivers[i].getNationality(),
                                                                'Number':self.drivers[i].getNumber(),
                                                                'Team':self.drivers[i].getTeam(),
                                                                'Tyre_Compound':self.drivers[i].getTyreCompound().getName(),
                                                                'Race_Time':race_time_timedelta,
                                                                'Lap_Time':lap_race_timedelta,
                                                                'Tyre_Age': tyre_age+1,

                                                        }

                                        positions.append(data)
                                number_of_laps_safety_car += 1
                                if number_of_laps_safety_car >= 5:
                                        self.circuit.setIsSCOut(False)
                                        


                        df = pd.DataFrame(positions)
                        df_dnf = pd.DataFrame(dnf)
                        df_sorted = df.sort_values(by='Race_Time', ascending=True).reset_index()
                        print(df_sorted['Race_Time'][0])
                        # datetime.strptime(date_time_str, '%d/%m/%y %H:%M:%S')

                        df_sorted['Gap_to_Leader'] =  pd.to_datetime(df_sorted['Race_Time'], format='%H:%M:%S.%f') - datetime.datetime.strptime(df_sorted['Race_Time'][0],'%H:%M:%S.%f')
                        df_sorted['Gap_to_Leader'] = '+' + df_sorted['Gap_to_Leader'].astype(str).map(lambda x: x[8:])

                        print("Lap: %i/%i" % (j,number_of_laps))
                        print(df_sorted)
                        print('------------------------------------------------------------------------------------------------------------------')
                        if len(df_dnf) > 0:
                                print(df_dnf)

                        print("Volta mais rápida: %s - %s" % (str(datetime.timedelta(seconds=max)), piloto_volta_mais_rapida))
                        input("Press Enter to continue...")
                df_sorted.to_excel('classificacao_final.xlsx', index=False)
                df_dnf.to_excel('dnf_cars.xlsx', index=False)        
