import pyrosim
import math
import random
from robot import ROBOT


class INDIVIDUAL:

    def __init__(self): 
        self.genome = random.random() * 2 - 1
        print(self.genome)
        self.fitness = 0

    def Evaluate(self): 
        sim = pyrosim.Simulator(play_blind=True, eval_time=1000, debug=False, play_paused= False, use_textures=True, xyz=[-25,-50,0])
        robot = ROBOT (sim, self.genome ) 
        sim.start()
        sim.wait_to_finish()

        x = sim.get_sensor_data( sensor_id = robot.Poshead , svi = 0 )
        y = sim.get_sensor_data( sensor_id = robot.Poshead , svi = 1 )
        z = sim.get_sensor_data( sensor_id = robot.Poshead , svi = 2 )
        #print("Sensor x", x[-1]+4.25)