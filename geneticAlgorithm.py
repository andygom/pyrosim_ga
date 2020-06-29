from robot import ROBOT
from individual import INDIVIDUAL
from population import POPULATION
import pyrosim
import random
import copy
import pickle

generations = 100

parents = POPULATION(5)
parents.Initialize()
parents.Evaluate()
parents.Print()


for g in range (0, generations):
    children = POPULATION(5)
    children.Evaluate()
    children.Fill_From(parents)
    
    exit()
#     children = copy.deepcopy(parents)
#     children.Mutate()
#     children.Evaluate()
#     parents.ReplaceWith(children)
#     print(g)
#     parents.Print()


# parent = INDIVIDUAL()
# parent.Evaluate(True)
# print(parent.fitness)

# for i in range (0, 500):
#     child = copy.deepcopy( parent )
#     child.Mutate()
#     child.Evaluate(True)
#     print('[g:' ,i , '] [p:' ,parent.fitness , ']', '[c:' ,child.fitness , ']')
#     if ( child.fitness > parent.fitness ):
#       parent = child
#       parent.Evaluate(True)
    
#     f = open('robot.p','wb')
#     pickle.dump(parent , f )
#     f.close()

