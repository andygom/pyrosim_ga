from robotRandom import ROBOT
from individualRandom import INDIVIDUAL
# from population import POPULATION
import pyrosim
import random
import copy
import pickle
import numpy as np
import matplotlib.pyplot as plt


fitvector =  [0 for c in range(300)] 
fitvectorAv = range(300)
print(fitvector)


for i in range(0,300):
    seconds = 100.0
    dt = 0.1
    eval_time = int(seconds/dt)
    gravity = -1.0
    sim = pyrosim.Simulator(play_blind=True, eval_time=eval_time,
                                     debug=False, play_paused=False, use_textures=True, xyz=[-25, -50, 0])
    robot = ROBOT(sim, np.random.rand(8, 2) * 2 - 1)
    sim.start()
    sim.wait_to_finish()
    xh =  sim.get_sensor_data(sensor_id=robot.Poshead, svi=0)
    xt =  sim.get_sensor_data(sensor_id=robot.Postail, svi=0)
    xb0 = sim.get_sensor_data(sensor_id=robot.Posbody0, svi=0)
    xb1 = sim.get_sensor_data(sensor_id=robot.Posbody1, svi=0)
    xb2 = sim.get_sensor_data(sensor_id=robot.Posbody2, svi=0)
    # y =  sim.get_sensor_data(sensor_id= robot.Poshead, svi=1)
    # z =  sim.get_sensor_data(sensor_id= robot.Poshead, svi=2)
    PosRobot = [4.25 +  xh[-1], 80.75 +  xt[-1], 23.5 +  xb0[-1], 41.5 +  xb1[-1], 59.5 +  xb2[-1]]
    fitness = sum(PosRobot) / len(PosRobot)
    # print(fitness)
    #  fitness = (4.25 +  xh[-1] + 80.75 +  xt[-1] ) / 2
    fitvector[i] = fitness

    # fitvectorAv[j] = np.average(fitvector[j])
    print(fitvector)


plt.bar(fitvectorAv, fitvector)
plt.ylabel('fitness')
plt.xlabel('individuals')
plt.show()
print(fitvector)