class Salesman:
   destinationCities = []
   
   def addCity(self, city):
      self.destinationCities.append(city)
   
   def get_city(self, index):
      return self.destinationCities[index]
   
   def numberOfCities(self):
      return len(self.destinationCities)