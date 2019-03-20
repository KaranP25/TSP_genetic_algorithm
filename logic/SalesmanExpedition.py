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
         for i in range(0, self.Salesman.num_of_cities()):
            self.tour.append(None)
   
   def __repr__(self):
      string = ""
      for i in range(0, self.tour_size()):
        string += " ["
        string += str(self.get_city(i))
        if(i==self.tour_size()-1):
            string += "]"
        else:
            string += "] ->"
      return string
   
   def generate_individual(self):
      for city_index in range(0, self.Salesman.num_of_cities()):
         self.set_city(city_index, self.Salesman.get_city(city_index))
      random.shuffle(self.tour)
   
   def get_city(self, tour_pos):
      return self.tour[tour_pos]
   
   def set_city(self, tour_pos, city):
      self.tour[tour_pos] = city
      self.fitness = 0.0
      self.distance = 0
   
   def get_fitness(self):
      if self.fitness == 0:
            self.fitness = 1/float(self.get_distance())
      return self.fitness
   
   def get_distance(self):
      if self.distance == 0:
         tour_distance = 0
         for city_index in range(0, self.tour_size()):
            from_city = self.get_city(city_index)
            destination_city = None
            if city_index+1 < self.tour_size():
               destination_city = self.get_city(city_index+1)
            else:
               destination_city = self.get_city(0)
            tour_distance += from_city.get_distance(destination_city)
         self.distance = tour_distance
      return self.distance
   
   def tour_size(self):
      return len(self.tour)
   
   def get_contained_city(self, city):
      return city in self.tour
   
   def get_tour(self):
      return self.tour