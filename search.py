from robot import ROBOT
from individual import INDIVIDUAL
import pyrosim
import random



for i in range (0, 3):
    individual = INDIVIDUAL()
    individual.Evaluate()
    print(individual.fitness)
    
