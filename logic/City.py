import math
import random

class City:
   def __init__(self, domain, id, x=None, y=None, distance_dict=None):
      self.x = None
      self.y = None
      self.distance_dict = dict()

      self.id = id
      self.domain = domain # 0=point data; 1=distance data
      
      if x is not None:
         self.x = x
      else:
         self.x = int(random.random() * 200)

      if y is not None:
         self.y = y
      else:
         self.y = int(random.random() * 200)

      if distance_dict is not None:
         self.distance_dict = distance_dict
   
   
   def set_distance_dict(self, dict):
      self.distance_dict = dict

   def get_distance_dict(self):
      return self.distance_dict

   def get_id(self):
      return self.id

   def get_x(self):
      return self.x
   
   def get_y(self):
      return self.y
   
   def get_distance(self, next_city):
      distance = 0
      if self.domain == 0:
         x_dist = abs(self.get_x() - next_city.get_x())
         y_dist = abs(self.get_y() - next_city.get_y())
         distance = math.sqrt( (x_dist ** 2) + (y_dist ** 2) )
         
      else:
         distance = float(self.distance_dict.get(str(next_city)))

      return distance
   
   def __repr__(self):
      if self.domain == 0:
         return str(self.get_id()) + ": " + str(self.get_x()) + ", " + str(self.get_y())
      else:
         return str(self.get_id())
