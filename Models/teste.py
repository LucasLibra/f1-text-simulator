from lap import Lap
from tyre import Tyre
import matplotlib.pyplot as plt

soft_tyre = Tyre(tyre_name = "Soft", tyre_speed = 0.01)
medium_tyre = Tyre(tyre_name = "Medium",tyre_speed = 0.03)
hard_tyre = Tyre(tyre_name = "Hard", tyre_speed = 0.05)

lap_average = 67
number_of_laps = 72
percurso = 5000
lap_soft_time = 0
lap_medium_time = 0
lap_hard_time = 0

lap_soft = Lap(lap_average = lap_average, tyre = soft_tyre)
lap_medium = Lap(lap_average = lap_average, tyre = medium_tyre)
lap_hard = Lap(lap_average = lap_average, tyre = hard_tyre)

for n in range(0,number_of_laps):
    lap_soft_partial_time = lap_soft.lap_performance(number_of_laps = n, percurso = percurso)
    lap_medium_partial_time = lap_medium.lap_performance(number_of_laps = n, percurso = percurso)
    lap_hard_partial_time = lap_hard.lap_performance(number_of_laps = n, percurso = percurso)

    lap_soft_time += lap_soft_partial_time
    lap_medium_time += lap_medium_partial_time
    lap_hard_time += lap_hard_partial_time
    plt.plot(n, lap_soft_time/(n+1), color='red', marker='o')
    plt.plot(n, lap_medium_time/(n+1), color='yellow', marker='x')
    plt.plot(n, lap_hard_time/(n+1), color='gray', marker='+')
    plt.pause(0.05)

print(lap_soft_time)
print(lap_medium_time)
print(lap_hard_time)
