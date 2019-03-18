import math
import random

class City:
   def __init__(self, city, id):
      self.city = city
      self.id = id
      self.distances = dict()

   def set_distance(self, id, distance):
      self.distances[id] = distance

   def get_distance(self, id):
      return self.distances[id]
