import numpy as np

class ParetoFrontGenerator:
  def __init__(self, function, translation=0):
    self.translation = translation
    self.function = function 
  def generate_space(self):
    space = self.function.get_space()
    space = space+self.translation
    space = space[(space <= 1).all(axis=1)]
    space = space[(space >= 0).all(axis=1)]
    return space

