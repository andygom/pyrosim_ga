from robot import ROBOT
from individual import INDIVIDUAL
import pyrosim
import math
import random
import copy 
import numpy as np
aaa


class POPULATION:

    def __init__(self, popSize): 
        self.popSize = popSize 
        self.p = {}
        for i in range(0,popSize): 
            self.p[i] = INDIVIDUAL(i)
        

    def Print(self):
        for i in self.p:
            if ( i in self.p ):
                self.p[i].Print()
        print()
        

    def Evaluate(self):
        for i in self.p:
            self.p[i].Start_Evaluation(True)
        for i in self.p:
            self.p[i].Compute_Fitness()

    def Mutate(self):
        for i in self.p:
            self.p[i].Mutate()

    def ReplaceWith(self,other):
        for i in self.p:
            if ( self.p[i].fitness < other.p[i].fitness ):
                self.p[i] = other.p[i]

    def Initialize(self): 
        for g in range (0, self.popSize):
            self.p[g] = INDIVIDUAL(g)
    
    def Fill_From(self , other):
        self.Copy_Best_From(other)
        self.Print()
        self.Collect_Children_From(other)
        self.Print()
    
    def Copy_Best_From(self, other):
        self.bestfit = -100
        i = 0
        for j in other.p:
          if ( other.p[j].fitness > self.bestfit ):
            self.bestfit = other.p[j].fitness 
            i = j
          self.p[0] = copy.deepcopy(other.p[i]) 