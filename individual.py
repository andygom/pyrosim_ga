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
from datetime import datetime

class INDIVIDUAL:

    def __init__(self, i):
        self.ID = i

#         self.genomeh = [ ([ 3.82543924e-03, -3.23329861e-01,  7.76264224e-01,  7.41083063e-02,
#     1.40465357e-03,  3.75879326e-04, -2.66398599e-04,  6.12370636e-03,
#    -7.23613561e-01,  2.23361378e-01,  8.81198153e-04,  4.67949412e-06,
#    -8.40317090e+00, -4.81653414e-02]),  ([ 8.21152790e-02, -4.89590191e-04, -2.28957565e+00,  1.42461405e-04,
#    -2.80835049e-03, -7.24268211e-04, -9.33911387e+00,  8.01476109e-01,
#    -2.48012854e+01,  4.72087450e-07, -4.91636132e-01, -7.94106324e-02,
#     7.63007990e-05,  3.36193755e-01]),  ([-8.65226424e-04,  1.10757305e-01,  3.27955477e+00, -4.29214712e+00,
#    -4.30599508e+00, -2.68243702e-03,  1.64293036e-01,  2.66601962e-01,
#    -3.71706572e-03,  1.45217260e-03,  4.51331008e-04, -1.16154385e+02,
#     5.98625866e-04, -3.25011935e-02]),  ([ 9.80838000e-05,  1.06818013e-02, -2.82126515e+00, -1.68932166e-02,
#     5.58114649e-02,  7.99531112e-02, -1.34729992e-02, -1.75672258e-02,
#    -5.61143898e-02,  7.37765652e-04, -1.92807300e+02,  6.29333129e+00,
#     1.78615756e+00, -2.05449344e-02]),  ([ 1.39652686e-02, -1.29943165e-03,  1.36873815e-03,  4.76007576e-04,
#     1.39013759e-06, -1.51599569e-02,  2.55538932e-01,  5.06659722e-02,
#     1.98832796e-04, -1.75832436e+00, -1.98887719e-03,  2.16381934e-01,
#    -2.12191116e-05,  1.77880014e-02]),  ([-2.87442638e-01,  3.13909519e-03, -8.48951087e-01,  1.82240954e-01,
#    -8.32245363e-03,  3.30167275e-03, -2.18040535e-01,  1.29487095e-03,
#    -6.83476335e-02,  3.84949763e+00,  5.28653046e-05,  2.86272921e-02,
#    -1.44103235e+00,  1.94002260e+01])]

#         self.genomehp = [ ([-8.08065887e-01,  7.58801500e+00,  1.79776433e-02, -1.06844392e-04,
#    -5.90518076e-02,  2.09498824e+01,  3.44275873e-04, -3.87170169e-04,
#    -4.34837997e-03,  4.49714752e+01, -1.19819977e-03, -9.69694504e-03,
#     5.32675976e-03,  1.38850798e+00]),  ([ 4.80979850e-06,  1.41305234e+00, -8.25210622e-05,  1.20458848e-01,
#     4.02450087e-01,  1.72956450e-03,  3.92618038e-02,  8.71232939e-03,
#    -1.43907874e-05, -2.97396445e-01,  3.51608845e+00,  2.35305082e-02,
#     1.27328754e-06,  5.72254563e-01]),  ([ 6.08637204e+00, -1.82704402e-03,  9.14794619e-02, -1.78072558e+01,
#    -1.06143647e-03, -1.75203938e-02, -7.99265323e-04, -9.98768334e+00,
#    -1.53319959e-02, -2.51363394e-01,  6.26381719e-03,  3.82047849e+00,
#    -9.59865579e-02, -3.96485392e-01]),  ([ 1.65182157e-01,  6.62507792e-01,  7.11366512e-02, -8.57945965e-02,
#    -1.26619898e-01,  1.83220664e-03, -2.81640920e+00, -1.39924631e-02,
#     4.82059881e-02, -2.38581807e+00,  2.75330094e-02,  5.01923773e-02,
#    -3.04170478e+00,  1.65090964e-01]),  ([-2.22479111e+00, -3.48638388e+00, -2.65465683e-08, -4.92109581e-02,
#    -3.47189796e-01,  6.72308631e-05,  5.14630213e+01,  6.63259713e-03,
#     7.79425654e-01, -1.85078010e-02,  8.52271531e-02,  1.52461353e-02,
#    -2.46562112e-03, -2.26178335e-06]),  ([ 8.11883413e-01, -1.12118273e-03, -6.64996107e-01,  4.47744860e-04,
#     3.25741158e-03,  3.56969231e-02, -1.15455301e-02, -8.03453345e-02,
#     1.14145799e-02, -1.40916805e-06,  3.55060866e-06,  1.14058586e-06,
#     2.58032675e-06,  1.47171328e-04]),  ([-8.40464617e-02,  3.53032600e+00, -5.82487179e-03,  3.81350562e-05,
#    -1.81279770e-02, -2.13774411e+01,  9.91069205e-01,  6.69855261e-02,
#    -4.98358376e-05, -1.76850842e-03, -8.78344745e-03,  4.50207071e-01,
#    -6.17703265e-02, -3.06256824e-06]),  ([ 4.50620170e+01, -3.89787218e-01, -1.17418555e-04,  2.75457482e-02,
#     6.60636588e-02, -6.96857767e-05,  1.77372817e-01, -1.47882437e+02,
#    -1.55880301e+00,  2.59335566e+00, -2.06765553e-02,  1.50748131e-02,
#    -5.82723580e-03, -1.48137253e-03])]

#         self.genomeo = [ ([-0.02246637, -1.56204898, -0.35311436,  0.86941048, -0.02717888,
#    -0.01222526, -0.03288468,  0.00853227]),  ([-5.61599009e+00, -9.13099710e-02, -4.05704145e-04, -4.75177448e-06,
#    -9.42922260e-01,  3.35231245e+01, -1.65329848e-06, -6.05378062e-03]),  ([ 5.34557291e-01,  2.42666825e-03,  8.45707314e-04,  1.84438287e+00,
#    -6.70932031e-03,  8.43620446e-03,  1.00616149e-04, -1.73642831e-02]),  ([-6.44616567e-06,  6.13743022e+01,  8.37530950e-02,  8.59863522e-02,
#    -2.89891357e-06, -2.96665931e-02,  2.58878414e-01, -1.95771579e-01]),  ([-2.68923249e-03, -5.23842341e-03, -8.41517388e-03, -3.08393476e-04,
#     2.97904441e-01,  2.74532521e-01, -2.38001944e+00,  2.85138337e-03]),  ([-3.16278695e-02, -6.23638181e-03, -3.56996987e-02,  6.38871027e+00,
#    -6.91702071e+00, -1.08349310e-01,  1.57196164e+02,  9.01105307e-05]),  ([ 1.50824146e-02, -2.04581742e+00, -1.54108297e-01,  7.33108435e-05,
#    -3.50906471e-01,  1.98114531e-05, -7.72933306e-02, -2.93392173e-03]),  ([-5.35565060e-01,  2.32238809e-03, -2.48453303e-04,  2.49236029e-03,
#    -4.95674618e-02, -2.12525445e+00, -1.89688576e-03, -2.11410593e-01]),  ([-1.17607844e-02, -3.10352716e-02,  3.90285398e-03, -4.16663067e-03,
#    -1.55308704e-04,  5.90337362e-01,  8.11494723e-05,  1.87861785e-04]),  ([-2.97857672e-03,  7.70391335e-01,  2.90259331e-03, -4.34377463e-01,
#    -2.37777576e-02,  7.21462450e-03, -2.87148003e-04, -3.16819998e-02]),  ([-9.25389064e-06, -1.31019393e-03, -4.64456763e-03, -9.75405036e-03,
#     3.77361814e-02,  1.43570142e-04,  4.78812502e-01, -1.47286313e-01]),  ([ 4.42444042e-05, -2.13066888e-01,  3.05378510e+00,  9.80317529e+00,
#     2.08483573e-01, -1.66301212e+00,  3.06844680e-05,  7.62770533e+00]),  ([ 2.88896299e-06, -2.66329391e-01, -1.68430670e-02,  2.83031593e-01,
#    -6.77106577e-05,  7.51714279e-04,  6.36676224e-03, -2.68016565e-03]),  ([ 2.29340958e-04, -3.81826367e+00, -3.98979510e-01, -1.05098034e-01,
#     3.86697865e-03, -6.15481416e-02, -1.02147197e-03, -1.58896297e-08])]


        self.genomeh = np.random.rand(6, 14) * 2 - 1
        self.genomehp = np.random.rand(8, 14) * 2 - 1
        self.genomeo = np.random.rand(14, 8) * 2 - 1
        self.fitness = 0


    def Start_Evaluation(self, pb):
        seconds = 200.0
        dt = 0.1
        eval_time = int(seconds/dt)
        gravity = -1.0
        self.sim = pyrosim.Simulator(play_blind=pb, eval_time=eval_time,
                                     debug=False, play_paused=False, use_textures=True, xyz=[-25, -50, 0], dt= 0.1)
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
        # self.fitness = (4.25 + self.xh[-1] + 80.75 + self.xt[-1] ) / 2
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
            if mutgen <= 3:
                genomeh[i] = random.gauss(genomeh[i], math.fabs(genomeh[i]))
                # self.genomeh[i] = random.gauss(self.genome[j], math.fabs[j])
        self.genomeh = np.split(genomeh, 6)

        for i in range (0, 112):
            mutgen = random.randint(0 ,100)
            if mutgen <= 3:
                genomehp[i] = random.gauss(genomehp[i], math.fabs(genomehp[i]))
                # self.genomeh[i] = random.gauss(self.genome[j], math.fabs[j])
        self.genomehp = np.split(genomehp, 8)

        for i in range (0, 112):
            mutgen = random.randint(0 ,100)
            if mutgen <= 3:
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
            pathNMew = str(datetime.now())
            os.mkdir(pathNMew)
            # G U A R D A R     EN CSV X GENERACION
            for x in range(0, gen+1):
                # savetxt("data"+str(x)+str(x+1)+".csv", genomehvector[x][i], delimiter=',')
                name = pathNMew+"/Gen"+str(x)+".csv"
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
