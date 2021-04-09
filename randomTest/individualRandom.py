import random
import numpy as np
import pyrosim
import math
from robotRandom import ROBOT
import matplotlib.pyplot as plt
import csv
from numpy import asarray
from numpy import savetxt
import os


class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i
        self.genomeh = np.random.rand(6, 14) * 2 - 1
        self.genomehp = np.random.rand(8, 14) * 2 - 1
        self.genomeo = np.random.rand(14, 8) * 2 - 1
        self.fitness = 0


    def Start_Evaluation(self, pb):
        seconds = 100.0
        dt = 0.1
        eval_time = int(seconds/dt)
        gravity = -1.0
        self.sim = pyrosim.Simulator(play_blind=pb, eval_time=eval_time,
                                     debug=False, play_paused=False, use_textures=True, xyz=[-25, -50, 0])
        # if len(self.genome) == 196:
        #     self.genomehidden = np.split(self.genome, 14)
        #     self.robot = ROBOT(self.sim, self.genome)
        #     self.sim.start()

        # self.robot = ROBOT (self.sim, self.genomehidden, self.genomeoutput )
        # self.robot = ROBOT(self.sim, self.genome)
        self.robot = ROBOT(self.sim, self.genomeh, self.genomehp, self.genomeo)
        self.sim.start()

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        self.xh = self.sim.get_sensor_data(sensor_id=self.robot.Poshead, svi=0)
        self.xt = self.sim.get_sensor_data(sensor_id=self.robot.Postail, svi=0)
        self.xb0 = self.sim.get_sensor_data(sensor_id=self.robot.Posbody0, svi=0)
        self.xb1 = self.sim.get_sensor_data(sensor_id=self.robot.Posbody1, svi=0)
        self.xb2 = self.sim.get_sensor_data(sensor_id=self.robot.Posbody2, svi=0)
        # y = self.sim.get_sensor_data(sensor_id=self.robot.Poshead, svi=1)
        # z = self.sim.get_sensor_data(sensor_id=self.robot.Poshead, svi=2)
        PosRobot = [4.25 + self.xh[-1], 80.75 + self.xt[-1], 23.5 + self.xb0[-1], 41.5 + self.xb1[-1], 59.5 + self.xb2[-1]]
        self.fitness = sum(PosRobot) / len(PosRobot)
        print(self.fitness)
        # self.fitness = (4.25 + self.xh[-1] + 80.75 + self.xt[-1] ) / 2
        del self.sim