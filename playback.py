from individual import INDIVIDUAL
import pickle
import numpy as np
import csv
import pandas
import pyrosim
from robot import ROBOT
import csv
import pprint

with open('/home/ambar/Documents/pyrosim-master/snakerobot/Gen0.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    genmehs = []
    genmehps = []
    genmeos = []
    inds = []
    for row in readCSV:
        ind = row[1]
        genmeh = row[2]
        genmehp = row[3]
        genmeo = row[4]

        genmehs.append(genmeh)
        genmehps.append(genmehp)
        genmeos.append(genmeo)
        inds.append(ind)

    # print(genmehs)
    # print(inds)

    # now, remember our lists?

    whatind = 5
    # coldex = inds.index(whatind)
    thegenmeh = genmehs[5]
    thegenmehp = genmehps[5]
    thegenmeo = genmeos[5]

    # genh = np.split(thegenmeh, 6)
    pprint.pprint(thegenmeh)
    print(np.array2string(thegenmeh, separator=', '))
    # print(thegenmehp)
    # print(thegenmeo)
    # print('The genmeh of',whatind,'is:',thegenmeh)

seconds = 120.0
dt = 0.2
eval_time = int(seconds/dt)
gravity = -1.0
sim = pyrosim.Simulator(play_blind=False, eval_time=eval_time,
                             debug=False, play_paused=False, use_textures=True, xyz=[-25, -50, 0])


robot = ROBOT(sim, thegenmeh, thegenmehp, thegenmeo)
sim.start()
sim.wait_to_finish()

# f = open ( 'robot.p' , 'rb' )
# best = pickle.load(f)

# f.close()

# # best.genomehidden =  best.genome[0:196]
# # best.genomehidden = np.split(best.genomehidden, 14)
# # best.genomeoutput = np.split(best.genome[196:308], 14)
# # print('genoma', best.genomeoutput)
# # print(np.random.rand(14, 8) * 2 -1)
# # print(best.genomehidden)
# best.Start_Evaluation(False)
# print(best.fitness)

