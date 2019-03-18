from logic.Population import Population
from logic.SalesmanExpedition import SalesmanExpedition
import random

class GA:
   def __init__(self, Salesman):
      self.Salesman = Salesman
      self.mutationRate = 0.015
      self.tournamentSize = 5
      self.elitism = True
   
   def evolvePopulation(self, pop):
      newPopulation = Population(self.Salesman, pop.getPopulationSize(), False)
      elitismOffset = 0
      if self.elitism:
         newPopulation.saveTour(0, pop.getFittest())
         elitismOffset = 1
      
      for i in range(elitismOffset, newPopulation.getPopulationSize()):
         parent1 = self.tournamentSelection(pop)
         parent2 = self.tournamentSelection(pop)
         child = self.crossover(parent1, parent2)
         newPopulation.saveTour(i, child)
      
      for i in range(elitismOffset, newPopulation.getPopulationSize()):
         self.mutate(newPopulation.getTour(i))
      
      return newPopulation
   
   def crossover(self, parent1, parent2):
      child = SalesmanExpedition(self.Salesman)
      
      startPos = int(random.random() * parent1.tour_size())
      endPos = int(random.random() * parent1.tour_size())
      
      for i in range(0, child.tour_size()):
         if startPos < endPos and i > startPos and i < endPos:
            child.set_city(i, parent1.get_city(i))
         elif startPos > endPos:
            if not (i < startPos and i > endPos):
               child.set_city(i, parent1.get_city(i))
      
      for i in range(0, parent2.tour_size()):
         if not child.get_contained_city(parent2.get_city(i)):
            for ii in range(0, child.tour_size()):
               if child.get_city(ii) == None:
                  child.set_city(ii, parent2.get_city(i))
                  break
      
      return child
   
   def mutate(self, tour):
      for tourPos1 in range(0, tour.tour_size()):
         if random.random() < self.mutationRate:
            tourPos2 = int(tour.tour_size() * random.random())
            
            city1 = tour.get_city(tourPos1)
            city2 = tour.get_city(tourPos2)
            
            tour.set_city(tourPos2, city1)
            tour.set_city(tourPos1, city2)
   
   """ Selects parent candidates of tour locations for crossover """
   def tournamentSelection(self, pop):
      tournament = Population(self.Salesman, self.tournamentSize, False)
      for i in range(0, self.tournamentSize):
         randomId = int(random.random() * pop.getPopulationSize())
         tournament.saveTour(i, pop.getTour(randomId))
      fittest = tournament.getFittest()
      return fittest
