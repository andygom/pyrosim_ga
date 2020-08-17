import random
import numpy as np
import pyrosim
import math
from robot import ROBOT
import matplotlib.pyplot as plt
import csv
from numpy import asarray
from numpy import savetxt
import os

class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i
        # self.genomehidden = np.random.rand(14, 14) * 2 - 1
        # self.genomeoutput = np.random.rand(14, 8) * 2 - 1
        # self.genome = np.append(self.genomehidden, self.genomeoutput)

        self.genomeh = np.random.rand(6, 14) * 2 - 1
        self.genomehp = np.random.rand(8, 14) * 2 - 1
        self.genomeo = np.random.rand(14, 8) * 2 - 1
        self.fitness = 0


    def Start_Evaluation(self, pb):
        seconds = 120.0
        dt = 0.2
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
        # PosRobot = [4.25 + self.xh[-1], 80.75 + self.xt[-1], 23.5 + self.xb0[-1], 41.5 + self.xb1[-1], 59.5 + self.xb2[-1]]
        # self.fitness = sum(PosRobot) / len(PosRobot)
        self.fitness = (4.25 + self.xh[-1] + 80.75 + self.xt[-1] ) / 2
        del self.sim

    # def Compute_Fitness(self):
    #   self.sim.wait_to_finish()
    #   # sensorData = self.sim.get_sensor_data( sensor_id = self.robot.Ray2 )
    #   # print(sensorData)
    #   x1 = self.sim.get_sensor_data( sensor_id =  self.snakeservo.Pos1, svi = 0 )
    #   y1 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Pos1 , svi = 1 )
    #   x2 = self.sim.get_sensor_data( sensor_id =  self.snakeservo.Pos2, svi = 0 )
    #   y2 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Pos2 , svi = 1 )
    #   xc0 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[0] , svi = 1 )
    #   xc1 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[1] , svi = 1 )
    #   xc2 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[2] , svi = 1 )
    #   xc3 = self.sim.get_sensor_data( sensor_id = self.snakeservo.Poscyl[3] , svi = 1 )

    #   # prop_sensor_results = self.sim.get_sensor_data(self.robot.Px[2])
    #   # print(prop_sensor_results)
    #   # self.fitness = x[-1]
    #   # max_item = max(y)
    #   # self.fitness = ( (1000-x1[-1]) + (1000-x2[-1] ) )/ 2
    #   # self.fitness = (x1[-1]+x2[-1])/2
    #   # print x1[-1], x2[-1]

    #   self.fitness = (xc0[-1] + (xc1[-1]-xc1[0]) + (xc2[-1]-xc2[0]) + (xc3[-1]-xc3[0]))   / 4

        # del self.sim

    def Mutate(self):
    #   for j in range(0, 308):
    #     mutgen = random.randint(0, 100)
    #     if mutge > 50:
    #       self.genome[j] = radom.gauss(self.genome[j], math.fabs[j])
        genomeh = np.concatenate(self.genomeh)
        genomehp = np.concatenate(self.genomehp)
        genomeo = np.concatenate(self.genomeo)

        for i in range (0, 84):
            mutgen = random.randint(0 ,100)
            if mutgen <= 6:
                genomeh[i] = random.gauss(genomeh[i], math.fabs(genomeh[i]))
                # self.genomeh[i] = random.gauss(self.genome[j], math.fabs[j])
        self.genomeh = np.split(genomeh, 6)

        for i in range (0, 112):
            mutgen = random.randint(0 ,100)
            if mutgen <= 6:
                genomehp[i] = random.gauss(genomehp[i], math.fabs(genomehp[i]))
                # self.genomeh[i] = random.gauss(self.genome[j], math.fabs[j])
        self.genomehp = np.split(genomehp, 8)

        for i in range (0, 112):
            mutgen = random.randint(0 ,100)
            if mutgen <= 6:
                genomeo[i] = random.gauss(genomeo[i], math.fabs(genomeo[i]))
                # self.genomeh[i] = random.gauss(self.genome[j], math.fabs[j])
        self.genomeo = np.split(genomeo, 14)
        
        # for i in range (0, 112):
        #     mutgen = random.randint(0 ,100)
        #     if mutgen > 3:
        #         self.genomehp[i] = random.gauss(self.genome[j], math.fabs[j])
        
        # for i in range (0, 112):
        #     mutgen = random.randint(0 ,100)
        #     if mutgen > 3:
        #         self.genomeo[i] = random.gauss(self.genome[j], math.fabs[j])
        
 

# inf de cada individuo de la poblacion print, plot fitness, save csv*

    def Print(self, i, popsize, fitvector, fitprom, genomehvector, genomehpvector, genomeovector, gen, g, generation):
        # print(self.genome)
        # print(self.fitness),
        print('[', self.ID, self.fitness, '] ', end='')
        # print "ID]",
        # print(self.ID),
        # print(self.fitness),
        # print(self.genome),
        # print("]"),
        # print i, gen
        fitvector[gen][i] = self.fitness
        # print genoma
        # best = [[0] for f in range (gen)]
        # print max(fitvector)

        genomehvector[gen][i] = self.genomeh
        genomehpvector[gen][i] = self.genomehp
        genomeovector[gen][i] = self.genomeo
        # genomevector[gen][i] = self.genome
        # print genomevector

        if g == gen+1 and i == popsize-1:
            
            # seconds = 120.0
            # dt = 0.2
            # eval_time = int(seconds/dt)
            # gravity = -1.0
            # sim = pyrosim.Simulator(play_blind=False, eval_time=eval_time,
            #                              debug=False, play_paused=False, use_textures=True, xyz=[-25, -50, 0])


            # robot = ROBOT(sim, genomehvector[gen][i], genomehpvector[gen][i], genomeovector[gen][i])
            # sim.start()
            # sim.wait_to_finish()

            # E N C O N T R A R   MEJOR INDIVIDUO
            best = 0
            self.gbest = 0
            self.ibest = 0
            for g in range(0, gen+1):
                for i in range(0, popsize):
                    fitness = fitvector[g][i]
                    if fitness > best:
                        best = fitness
                        self.gbest = g
                        self.ibest = i

            seconds = 120.0
            dt = 0.2
            eval_time = int(seconds/dt)
            gravity = -1.0
            sim = pyrosim.Simulator(play_blind=False, eval_time=eval_time,
                                         debug=False, play_paused=False, use_textures=True, xyz=[-25, -50, 0])
            robot = ROBOT(sim, genomehvector[self.gbest][self.ibest], genomehpvector[self.gbest][self.ibest], genomeovector[self.gbest][self.ibest])
            sim.start()

            # P R O M E D I O    FITNESS X GENERACION
            for x in range(0, gen+1):
                #   print fitprom
                fitprom[x][0] = sum(fitvector[x])/popsize
                generation[x][0] = x
                # print fitprom

            # S A V E in .npz
            # np.save
            # filename = "/home/ambar/Documents/individual/"+"Gen"+str(x)
            # os.makedirs(os.path.dirname(filename), exist_ok=True)
            # file = "/home/ambar/Documents/individual/"+"Gen"+str(x) + "/" + "genomehvector.npy"
            # np.save(file, genomehvector)
            # G U A R D A R     EN CSV X GENERACION
            for x in range(0, gen+1):
                # savetxt("data"+str(x)+str(x+1)+".csv", genomehvector[x][i], delimiter=',')
                name = "Gen"+str(x)+".csv"
                with open(name, mode='w') as csv_file:
                    fieldnames = ['gen', 'ind', 'genomeh', 'genomehp', 'genomeo', 'fitness']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    for i in range(0, popsize):
                        writer.writerow(
                            {'gen': x, 'ind': i, 'genomeh': genomehvector[x][i], 'genomehp': genomehpvector[x][i], 'genomeo': genomeovector[x][i], 'fitness': fitvector[x][i]})

            #  P L O T
            f = plt.figure()
            panel = f.add_subplot(111)
            plt.plot(generation, fitprom)
            print(max(fitprom), min(fitprom))
            # plt.axis(0, max(fitprom[-1]), 0, len(generation))
            plt.show()

    def PrintBest(self):
        # print(self.genome)
        # print(self.fitness),
        # print(self.genomehidden, self.genomeoutput)
        # print(self.genomeh),
        # print(self.genomeop),
        print("["),
        print(self.ID),
        print(self.fitness),
        print("]"),
        f = open("bestind.txt", "a")
        np.savetxt("bestind.txt", self.genomeh, self.genomeop)
        f.close()

        with open('Best.csv', mode='w') as csv_file:
            fieldnames = ['genomeh', 'genomeop', 'fitness']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(
                {'genome': self.genomeh, 'genomeop': self.genomeop, 'fitness': self.fitness})


# from robot import ROBOT
# import pyrosim
# import math
# import random
# import numpy as np


# class INDIVIDUAL:

#     def __init__(self, i):
#         self.ID = i
#         self.genomehidden = np.random.rand(14, 14) * 2 -1
#         self.genomeoutput = np.random.rand(14, 8) * 2 -1
#         self.genome = np.append(self.genomehidden, self.genomeoutput)
            # self.fitness = 0

#     def Start_Evaluation(self, pb):
#         seconds = 120.0
#         dt = 0.2
#         eval_time = int(seconds/dt)
#         gravity = -1.0
#         self.sim = pyrosim.Simulator(play_blind=pb, eval_time=eval_time, debug=False, play_paused= False, use_textures=True, xyz=[-25,-50,0])
#         self.robot = ROBOT (self.sim, self.genomehidden, self.genomeoutput )
#         self.sim.start()

#     def Compute_Fitness(self):
#         self.sim.wait_to_finish()
#         self.xh = self.sim.get_sensor_data( sensor_id = self.robot.Poshead , svi = 0 )
#         self.xt = self.sim.get_sensor_data( sensor_id = self.robot.Postail , svi = 0 )
#         y = self.sim.get_sensor_data( sensor_id = self.robot.Poshead , svi = 1 )
#         z = self.sim.get_sensor_data( sensor_id = self.robot.Poshead , svi = 2 )
#         self.fitness = (self.xh[-1])
#         del self.sim

#     #verificar mutacion
#     def Mutate(self):
#         for j in range (0, 13):
#           for i in range (0, 13):
#             mutgen = random.randint(0, 1000)
#             if mutgen < 130 :
#               self.genomehidden[j][i] = random.gauss( self.genomehidden[j][i] , math.fabs(self.genomehidden[j][i]))
#         for j in range (0, 13):
#           for i in range (0, 7):
#             mutgen = random.randint(0, 1000)
#             if mutgen < 130 :
#               self.genomeoutput[j][i] = random.gauss( self.genomeoutput[j][i] , math.fabs(self.genomeoutput[j][i]))
#         for j in range (0, 13):
#           for i in range (0, 13):
#             mutgen = random.randint(0, 1000)
#             if mutgen < 130 :
#               self.genomehidden[j][i] = random.gauss( self.genomehidden[j][i] , math.fabs(self.genomehidden[j][i]))
#         for j in range (0, 13):
#           for i in range (0, 7):
#             mutgen = random.randint(0, 1000)
#             if mutgen < 130 :
#               self.genomeoutput[j][i] = random.gauss( self.genomeoutput[j][i] , math.fabs(self.genomeoutput[j][i]))

#     def Print(self):
#         print('[',self.ID, self.fitness, '] ', end= '')
