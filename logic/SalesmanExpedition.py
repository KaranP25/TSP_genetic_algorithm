from logic.Salesman import Salesman
import random

class SalesmanExpedition:
   def __init__(self, Salesman, tour=None):
      self.Salesman = Salesman
      self.tour = []
      self.fitness = 0.0
      self.distance = 0
      if tour is not None:
         self.tour = tour
      else:
         for i in range(0, self.Salesman.numberOfCities()):
            self.tour.append(None)
   
   """ def __len__(self):
      return len(self.tour)
   
   def __getitem__(self, index):
      return self.tour[index]
   
   def __setitem__(self, key, value):
      self.tour[key] = value """
   
   def __repr__(self):
      geneString = ""
      for i in range(0, self.tour_size()):
        geneString += " ["
        geneString += str(self.get_city(i))
        if(i==self.tour_size()-1):
            geneString += "]"
        else:
            geneString += "] ->"
      return geneString
   
   def generate_individual(self):
      for cityIndex in range(0, self.Salesman.numberOfCities()):
         self.set_city(cityIndex, self.Salesman.get_city(cityIndex))
      random.shuffle(self.tour)
   
   def get_city(self, tourPosition):
      return self.tour[tourPosition]
   
   def set_city(self, tourPosition, city):
      self.tour[tourPosition] = city
      self.fitness = 0.0
      self.distance = 0
   
   def get_fitness(self):
      if self.fitness == 0:
            self.fitness = 1/float(self.get_distance())
      return self.fitness
   
   def get_distance(self):
      if self.distance == 0:
         tourDistance = 0
         for cityIndex in range(0, self.tour_size()):
            fromCity = self.get_city(cityIndex)
            destination_city = None
            if cityIndex+1 < self.tour_size():
               destination_city = self.get_city(cityIndex+1)
            else:
               destination_city = self.get_city(0)
            tourDistance += fromCity.get_distance(destination_city)
         self.distance = tourDistance
      return self.distance
   
   def tour_size(self):
      return len(self.tour)
   
   def get_contained_city(self, city):
      return city in self.tour