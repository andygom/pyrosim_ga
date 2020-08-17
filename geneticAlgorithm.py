from robot import ROBOT
from individual import INDIVIDUAL
from population import POPULATION
import pyrosim
import random
import copy
import pickle


popSize = 70
gen =  400


fitvector = [ [0 for c in range(popSize)] for f in range (gen)]
genomehvector = [ [0 for c in range(popSize)] for f in range (gen)]
genomehpvector = [ [0 for c in range(popSize)] for f in range (gen)]
genomeovector = [ [0 for c in range(popSize)] for f in range (gen)]
fitprom = [ [0] for f in range (gen)]   
generation = [ [0] for f in range (gen)] 

parents = POPULATION(popSize, 0, fitvector, genomehvector, genomehpvector, genomeovector, fitprom, gen, generation)
parents.Initialize()
parents.Evaluate()
print(0),
parents.Print()

for g in range(1, gen):
    children = POPULATION(popSize, g, fitvector, genomehvector, genomehpvector, genomeovector, fitprom, gen, generation)
    children.Fill_From(parents)
    children.Evaluate()
    print(g),
    children.Print()
    parents.p = children.p

    
# f= open('robot.p', 'w')
# pickle.dump (parents.p[0], f)
# f.close()


# generations = 5
# population = 10

# parents = POPULATION(population)
# parents.Initialize()
# parents.Evaluate()
# parents.Print()

# for g in range (0, generations):
#     print (g)
#     childrens = POPULATION(population)
#     childrens.Evaluate()
#     childrens.Fill_From(parents)

#     f = open('robot.p','wb')
#     pickle.dump(childrens.p[0] , f )
#     f.close()


    
    # exit()
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

