from robot import ROBOT
from individual import INDIVIDUAL
import pyrosim
import math
import random
import copy 
import numpy as np


class POPULATION:

    def __init__(self, popSize, gen, fitvector, genomehvector, genomehpvector, genomeovector, fitprom, g, generation):
          self.p = {}
          self.gen = gen
          self.g = g 
          self.fitvector = fitvector
          self.genomehvector = genomehvector
          self.genomehpvector = genomehpvector
          self.genomeovector = genomeovector
          self.fitprom = fitprom
          self.generation = generation
          # print self.fitvector
          # print self.genomevector
          # print gen
          self.popSize = popSize
          # self.fitvector= [ [0 for c in range(popSize)] for f in range (self.gen)]
          # print self.fitvector

    def Initialize(self):
      for i in range(0, self.popSize):
        self.p[i] = INDIVIDUAL(i)

    def Print(self):
        self.best = -5
        self.posbest = 0
        self.genbest = 0
        
        for i in self.p:
          if ( i in self.p ):
            self.p[i].Print(i, self.popSize, self.fitvector, self.fitprom, self.genomehvector, self.genomehpvector, self.genomeovector, self.gen, self.g ,self.generation)

        #     if self.p[i].fitness > self.best:
        #       self.best = self.p[i].fitness
        #       self.posbest = i
        #       self.genbest = self.gen
        # print self.posbest, self.genbest, self.best

        print ("")
    
    #   for i in self.p:
    #     if ( i in self.p ):
    #       self.p[i].Print(i, self.popSize, self.fitvector, self.fitprom, self.genomevector, self.gen, self.g)

    #     #     if self.p[i].fitness > self.best:
    #     #       self.best = self.p[i].fitness
    #     #       self.posbest = i
    #     #       self.genbest = self.gen
    #     # print self.posbest, self.genbest, self.best

    #   print ("")       
    # def Print(self):
    #     for i in self.p:
    #         if ( i in self.p ):
    #             self.p[i].Print()
    #     print()
        
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
        for g in range (0, self.popSize ):
            self.p[g] = INDIVIDUAL(g)
    
    def Fill_From(self , other):
        self.Copy_Best_From(other)
        # self.Print()
        self.Collect_Children_From(other)
        # self.Print()
    
    def Copy_Best_From(self, other):
        self.bestfit = -100
        i = 0
        for j in other.p:
          if (other.p[j].fitness > self.bestfit):
            self.bestfit = other.p[j].fitness 
            i = j
          self.p[0] = copy.deepcopy(other.p[i]) 
          
    def Collect_Children_From(self, other):
        for i in range(0, self.popSize, 2):
          winnergenome0, winnergenome1 = other.Winner_Of_Tournament_Selection(other, i)
          self.p[i] = copy.deepcopy(winnergenome0) 
          self.p[i].Mutate()
          self.p[i+1] = copy.deepcopy(winnergenome1) 
          self.p[i+1].Mutate()  

    
    def Winner_Of_Tournament_Selection(self, other, i):

      p0 = random.randint(0, self.popSize-1)
      p1 = random.randint(0, self.popSize-1)
      while p0 == p1:
        p0 = random.randint(0, self.popSize-1) 
      else: 
        if (other.p[p0].fitness > other.p[p1].fitness):
          newp0 = p0
        else: 
          newp0 = p1
      p2 = random.randint(0, self.popSize-1)
      p3 = random.randint(0, self.popSize-1)
      while p2 == p3:
        p2 = random.randint(0, self.popSize-1) 
      else: 
        if (other.p[p2].fitness > other.p[p3].fitness):
          # print(p2, other.p[p2].fitness, p3, other.p[p3].fitness)
          newp1 = p2
        else: 
          newp1 = p3
      genomewinner0 = copy.deepcopy(other.p[newp0])
      genomewinner1 = copy.deepcopy(other.p[newp1])
          
     # print('hidden', other.p[newp0].genomehidden, 'op', other.p[newp0].genomeoutput)
      # print('genome0', genomewinner0.genome)
      # print('genome1', genomewinner1.genome)

      genomeh0 = np.concatenate(genomewinner0.genomeh)
      genomehp0 = np.concatenate(genomewinner0.genomehp)
      genomeoutput0 = genomewinner0.genomeo

      genomeinput0 = np.append(genomeh0, genomehp0)
      

      genomeh1 = np.concatenate(genomewinner1.genomeh)
      genomehp1 = np.concatenate(genomewinner1.genomehp)
      genomeoutput1 = genomewinner1.genomeo

      genomeinput1 = np.append(genomeh1, genomehp1)

      pointCrossing0 = random.randint(0, 308)

      # cruce en capa inputs
      if (pointCrossing0 <= 196):

        newgenomeinput00 = genomeinput0[0:pointCrossing0]
        newgenomeinput01 = genomeinput1[pointCrossing0:196]

        newgenomeinput11 = genomeinput1[0:pointCrossing0]
        newgenomeinput10 = genomeinput0[pointCrossing0:196]

        wingenomeinput0 = np.append(newgenomeinput00, newgenomeinput01)
        
        wingenomeh0 = wingenomeinput0[0:84:]
        winnergenomeh0 = np.split(wingenomeh0, 6)
        wingenomehp0 = wingenomeinput0[84:196:]
        winnergenomehp0 = np.split(wingenomehp0, 8)

        wingenomeinput1 = np.append(newgenomeinput11, newgenomeinput10)

        wingenomeh1 = wingenomeinput1[0:84:]
        winnergenomeh1 = np.split(wingenomeh1, 6)
        wingenomehp1 = wingenomeinput1[84:196:]
        winnergenomehp1 = np.split(wingenomehp1, 8)

        genomewinner1.genomeh = winnergenomeh0
        genomewinner1.genomehp = winnergenomehp0

        genomewinner0.genomeh = winnergenomeh1
        genomewinner0.genomehp = winnergenomehp1

        return genomewinner0, genomewinner1

      # cruce en capa output
      if (pointCrossing0 > 196 and pointCrossing0 <= 308):

        # genomeoutput0 = np.append(newgenomeoutput00, newgenomeoutput01)

        newgenomeoutput00 = genomeoutput0[0:pointCrossing0]
        newgenomeoutput01 = genomeoutput0[pointCrossing0:112]
        genomewinnero0 = np.append(newgenomeoutput00, newgenomeoutput01)
        winnergenomeoutput0 = np.split(genomewinnero0, 14)
        # newgenomeoutput00 = genomeoutput0[0:pointCrossing0]
        # newgenomeoutput01 = genomeoutput1[pointCrossing0:308]

        # newgenomeoutput11 = genomeoutput1[0:pointCrossing0]
        # newgenomeoutput10 = genomeoutput0[pointCrossing0:308]

        # winnergenomeoutput0 = np.append(newgenomeoutput00, newgenomeoutput01)

        # winnergenomeoutput1 = np.append(newgenomeoutput11, newgenomeoutput10)

        genomewinner0.genomeo = winnergenomeoutput0
        genomewinner1.genomeo = winnergenomeoutput0

        return genomewinner0, genomewinner1



      # b = np.concatenate(genomewinner0.genomeh)
      # print(b)

      # new = b[0:10:]
      # print(new)

      # if (pointCrossing0 <= 84):
      #   nmutationGenome(pointCrossing0, genomewinner0, genomewinner1)   
      # if (pointCrossing0 > 84 and pointCrossing0 <= 196):
      #   print ('ok')   
      # if (pointCrossing0 > 196 and pointCrossing0 <= 308):
      #   print ('ok')   
      
    
    # def nmutationGenome(pointCross, genomewinner0, genomewinner1):
      
    #   newgenome00 = genomewinner0.genomeh[0:pointCrossing0]
    #   newgenome01 = genomewinner1.genomeh[pointCrossing0:308]

      # newgenome11 = genomewinner1.genome[0:pointCrossing0]
      # newgenome10 = genomewinner0.genome[pointCrossing0:308]
      

      # winnergenome0 = np.append(newgenome00, newgenome01)

      # winnergenomehidden0 = winnergenome0[0:196]
      # winnergenomeoutput0 = winnergenome0[196:308]

      # genomewinner0.genomehidden = winnergenomehidden0
      # genomewinner0.genomeoutput = winnergenomeoutput0

      # winnergenome1 = np.append(newgenome11, newgenome10)

      # winnergenomehidden1 = winnergenome1[0:196]
      # winnergenomehidden1 = np.split(winnergenomehidden1, 14)
      # winnergenomeoutput1 = winnergenome1[196:308]

      # genomewinner1.genomehidden = winnergenomehidden1
      # genomewinner1.genomeoutput = winnergenomeoutput1

      # # print(winnergenome0)
      # # print(np.split(winnergenome0, 2, 0))

      # # print(
      # # winnergenome1)




      # genomewinner1.genomeop = newgenomeop1
      # genomewinner2.genomeop = newgenomeop2
      # return genomewinner0, genomewinner1
