from logic.Population import Population
from logic.SalesmanExpedition import SalesmanExpedition
import random

class GA:
   def __init__(self, Salesman):
      self.Salesman = Salesman
      self.mutation_rate = 0.015
      self.tournament_size = 5
      self.elitism = True
   
   def evolve(self, curr_pop):
      new_population = Population(self.Salesman, curr_pop.get_population_size(), False)
      elitismOffset = 0
      if self.elitism:
         new_population.save_tour(0, curr_pop.get_fittest())
         elitismOffset = 1
      
      for pos_population in range(elitismOffset, new_population.get_population_size()):
         parent1 = self.tournament_selection(curr_pop)
         parent2 = self.tournament_selection(curr_pop)
         child = self.crossover(parent1, parent2)
         new_population.save_tour(pos_population, child)
      
      for pos_population in range(elitismOffset, new_population.get_population_size()):
         self.mutate(new_population.get_tour(pos_population))
      
      return new_population
   
   def crossover(self, parent1, parent2):
      child = SalesmanExpedition(self.Salesman)
      
      start_pos = int(random.random() * parent1.tour_size())
      end_pos = int(random.random() * parent1.tour_size())
      
      for pos_population in range(0, child.tour_size()):
         if start_pos < end_pos and pos_population > start_pos and pos_population < end_pos:
            child.set_city(pos_population, parent1.get_city(pos_population))
         elif start_pos > end_pos:
            if not (pos_population < start_pos and pos_population > end_pos):
               child.set_city(pos_population, parent1.get_city(pos_population))
      
      for pos_population in range(0, parent2.tour_size()):
         if not child.get_contained_city(parent2.get_city(pos_population)):
            for child_city in range(0, child.tour_size()):
               if child.get_city(child_city) == None:
                  child.set_city(child_city, parent2.get_city(pos_population))
                  break
      
      return child
   
   def mutate(self, tour):
      for tour_pos1 in range(0, tour.tour_size()):
         if random.random() < self.mutation_rate:
            tour_pos2 = int(tour.tour_size() * random.random())
            
            city_1 = tour.get_city(tour_pos1)
            city_2 = tour.get_city(tour_pos2)
            
            tour.set_city(tour_pos2, city_1)
            tour.set_city(tour_pos1, city_2)
   
   """ Selects parent candidates of tour locations for crossover """
   def tournament_selection(self, curr_pop):
      tournament = Population(self.Salesman, self.tournament_size, False)
      for pos_population in range(0, self.tournament_size):
         rand_id = int(random.random() * curr_pop.get_population_size())
         tournament.save_tour(pos_population, curr_pop.get_tour(rand_id))
      fittest = tournament.get_fittest()
      return fittest
