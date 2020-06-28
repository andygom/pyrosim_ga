from robot import ROBOT
import pyrosim
import math
import random
import numpy as np



class INDIVIDUAL:

    def __init__(self): 
        self.genomehidden = np.random.rand(14, 14)
        self.genomeoutput = np.random.rand(14, 8)
        # print(self.genome)
        

    def Evaluate(self, pb): 
        sim = pyrosim.Simulator(play_blind=pb, eval_time=1000, debug=False, play_paused= False, use_textures=True, xyz=[-25,-50,0])
        robot = ROBOT (sim, self.genomehidden, self.genomeoutput ) 
        sim.start()
        sim.wait_to_finish()

        self.x = sim.get_sensor_data( sensor_id = robot.Poshead , svi = 0 )
        y = sim.get_sensor_data( sensor_id = robot.Poshead , svi = 1 )
        z = sim.get_sensor_data( sensor_id = robot.Poshead , svi = 2 )
        self.fitness = self.x[-1]+4.25
        #print("Sensor x", x[-1]+4.25)

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