from lap import Lap
from tyre import Tyre
from circuito import Circuit
from classificacao import Qualifying
from corrida import Race
from drivers import Driver
import matplotlib.pyplot as plt
import pandas as pd

soft_tyre = Tyre(tyre_name = "Soft", tyre_speed = 0.01)
medium_tyre = Tyre(tyre_name = "Medium",tyre_speed = 0.05)
hard_tyre = Tyre(tyre_name = "Hard", tyre_speed = 0.09)

tyres = [soft_tyre, medium_tyre, hard_tyre]

circuits = []
drivers = []

df_circuits = pd.read_excel("../circuits.xlsx")
df_drivers = pd.read_excel('../drivers.xlsx')

for index, row in df_circuits.iterrows():
    circuit = Circuit(
        name = row['Name'],
        lap_average = row['Lap_average'],
        number_of_laps = row['Number_of_laps'],
        percurso = row['Percurso']
    )
    circuits.append(circuit)

for index, row in df_drivers.iterrows():
    tyre_compound = row['Tyre_Compound']
    for n in range(0,len(tyres)):
        if tyres[n].getName() == tyre_compound:
            tyre_compound = tyres[n]
    driver = Driver(
        name = row['Name'],
        team = row['Team'],
        tyre_compound = tyre_compound,
        tyre_age = row['Tyre_Age'],
        number = row['Number'],
        nationality = row['Nationality']
    )
    drivers.append(driver)


while True:
    circuito_name = input("Qual o nome do circuito?: ")
    for i in range(0,len(circuits)):
        if circuits[i].getName() == circuito_name:
            Circuito = circuits[i]

    menu = "Seja Bem vindo ao menu, deseja realizar o que? \n 1 - Classificação \n 2 - Corrida"
    print(menu)
    op = int(input("Escolha: "))
    if op == 1:
        qualy = Qualifying(circuit = Circuito, drivers = drivers)
        qualy.classificacao()
    elif op == 2:
        race = Race(circuit = Circuito, drivers = drivers, tyres = tyres)
        race.race()
    
