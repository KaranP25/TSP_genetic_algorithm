from logic.SalesmanExpedition import SalesmanExpedition

class Population:
   def __init__(self, Salesman, populationSize, initialise):
      self.tours = []
      for i in range(0, populationSize):
         self.tours.append(None)
      
      if initialise:
         for i in range(0, populationSize):
            newTour = SalesmanExpedition(Salesman)
            newTour.generate_individual()
            self.saveTour(i, newTour)
      
   def __setitem__(self, key, value):
      self.tours[key] = value
   
   def __getitem__(self, index):
      return self.tours[index]
   
   def saveTour(self, index, tour):
      self.tours[index] = tour
   
   def getTour(self, index):
      return self.tours[index]
   
   def getFittest(self):
      fittest = self.tours[0]
      for i in range(0, self.getPopulationSize()):
         if fittest.get_fitness() <= self.getTour(i).get_fitness():
            fittest = self.getTour(i)
      return fittest
   
   def getPopulationSize(self):
      return len(self.tours)
