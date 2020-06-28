from robot import ROBOT
from individual import INDIVIDUAL
import pyrosim
import math
import random
import numpy as np



class POPULATION:

    def __init__(self, popSize): 
        self.p = {}
        for i in range(0,popSize): 
            self.p[i] = INDIVIDUAL(i)
        

    def Print(self):
        for i in self.p:
            self.p[i].Print()

    def Evaluate(self):
        for i in self.p:
            self.p[i].Start_Evaluation(True)
        for i in self.p:
            self.p[i].Compute_Fitness()