from robot import ROBOT
from individual import INDIVIDUAL
import pyrosim
import random
import copy
import pickle

parent = INDIVIDUAL()
parent.Evaluate(True)
print(parent.fitness)

for i in range (0, 500):
    child = copy.deepcopy( parent )
    child.Mutate()
    child.Evaluate(True)
    print('[g:' ,i , '] [p:' ,parent.fitness , ']', '[c:' ,child.fitness , ']')
    if ( child.fitness > parent.fitness ):
      parent = child
      parent.Evaluate(True)
    
    f = open('robot.p','wb')
    pickle.dump(parent , f )
    f.close()

