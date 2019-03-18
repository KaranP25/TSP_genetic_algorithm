import math
import random

class City:
   def __init__(self, id, x=None, y=None):
      self.x = None
      self.y = None
      self.id = id

      if x is not None:
         self.x = x
      else:
         self.x = int(random.random() * 200)

      if y is not None:
         self.y = y
      else:
         self.y = int(random.random() * 200)
   
   def get_id(self):
      return self.id

   def get_x(self):
      return self.x
   
   def get_y(self):
      return self.y
   
   def get_distance(self, next_city):
      x_dist = abs(self.get_x() - next_city.get_x())
      y_dist = abs(self.get_y() - next_city.get_y())
      distance = math.sqrt( (x_dist ** 2) + (y_dist ** 2) )
      return distance
   
   def __repr__(self):
      return str(self.get_id()) + ": " + str(self.get_x()) + ", " + str(self.get_y())
