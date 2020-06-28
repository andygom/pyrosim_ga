from robot import ROBOT
import pyrosim
import math
import random
import numpy as np



class INDIVIDUAL:

    def __init__(self, i): 
        self.ID = i
        self.genomehidden = np.random.rand(14, 14)
        self.genomeoutput = np.random.rand(14, 8)
        # print(self.genome)
        

    def Start_Evaluation(self, pb): 
        self.sim = pyrosim.Simulator(play_blind=pb, eval_time=1000, debug=False, play_paused= False, use_textures=True, xyz=[-25,-50,0])
        self.robot = ROBOT (self.sim, self.genomehidden, self.genomeoutput ) 
        self.sim.start()
        

    def Compute_Fitness(self):
        self.sim.wait_to_finish()
        self.xh = self.sim.get_sensor_data( sensor_id = self.robot.Poshead , svi = 0 )
        self.xt = self.sim.get_sensor_data( sensor_id = self.robot.Postail , svi = 0 )
        y = self.sim.get_sensor_data( sensor_id = self.robot.Poshead , svi = 1 )
        z = self.sim.get_sensor_data( sensor_id = self.robot.Poshead , svi = 2 )
        self.fitness = (self.xh[-1]+self.xt[-1])/2+4.25
        del self.sim
       

    #verificar mutacion
    def Mutate(self): 
        for j in range (0, 13):
          for i in range (0, 13):
            mutgen = random.randint(0, 1000)
            if mutgen < 130 :
              self.genomehidden[j][i] = random.gauss( self.genomehidden[j][i] , math.fabs(self.genomehidden[j][i]))
        for j in range (0, 13):
          for i in range (0, 7):
            mutgen = random.randint(0, 1000)
            if mutgen < 130 :
              self.genomeoutput[j][i] = random.gauss( self.genomeoutput[j][i] , math.fabs(self.genomeoutput[j][i]))          
        for j in range (0, 13):
          for i in range (0, 13):
            mutgen = random.randint(0, 1000)
            if mutgen < 130 :
              self.genomehidden[j][i] = random.gauss( self.genomehidden[j][i] , math.fabs(self.genomehidden[j][i]))
        for j in range (0, 13):
          for i in range (0, 7):
            mutgen = random.randint(0, 1000)
            if mutgen < 130 :
              self.genomeoutput[j][i] = random.gauss( self.genomeoutput[j][i] , math.fabs(self.genomeoutput[j][i]))        


    def Print(self):
        print('[',self.ID, self.fitness, '] ', end= '')
