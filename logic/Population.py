from logic.SalesmanExpedition import SalesmanExpedition

class Population:
   def __init__(self, Salesman, size_population, is_initialise):
      self.tours = []
      for i in range(0, size_population):
         self.tours.append(None)
      
      if is_initialise:
         for i in range(0, size_population):
            new_tour = SalesmanExpedition(Salesman)
            new_tour.generate_individual()
            self.save_tour(i, new_tour)
      
   """ def __setitem__(self, key, value):
      self.tours[key] = value
   
   def __getitem__(self, index):
      return self.tours[index] """
   
   def save_tour(self, index, tour):
      self.tours[index] = tour
   
   def get_tour(self, index):
      return self.tours[index]
   
   def get_fittest(self):
      fittest = self.tours[0]
      for i in range(0, self.get_population_size()):
         if fittest.get_fitness() <= self.get_tour(i).get_fitness():
            fittest = self.get_tour(i)
      return fittest
   
   def get_population_size(self):
      return len(self.tours)
