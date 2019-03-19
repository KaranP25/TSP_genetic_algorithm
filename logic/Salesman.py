class Salesman:
   dest_cities = []
   
   def add_city(self, city):
      self.dest_cities.append(city)
   
   def get_city(self, index):
      return self.dest_cities[index]
   
   def num_of_cities(self):
      return len(self.dest_cities)