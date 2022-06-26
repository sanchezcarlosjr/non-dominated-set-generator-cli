import numpy as np
from .monotic_decreasing_functions import Polynomial

def normalize_by_l2(matrix):
  return matrix / np.linalg.norm(matrix, axis=-1)[:, np.newaxis]

class ParetoFrontGenerator:
  def __init__(self, dim=2, points=5, translation=0, function=Polynomial()):
    self.dim = dim
    self.points = points
    self.translation = translation
    self.function = function 
  def search(self):
      points = self.points
      while True:
            pareto_front = self.generate_space()
            if abs(self.points-pareto_front.shape[0])/self.points <= 0.1:
                return pareto_front
            points += 1
  def generate_space(self):
    fs = []
    for n in range(0, self.dim-1):
      fs.append(self.meshgrid(self.function.get_domain(self.points)))
    fs.append(self.function.get_image(np.array(fs)))
    fs = np.array(fs)
    space= normalize_by_l2(fs)
    space = space.T
    space = space+self.translation
    space = space[(space <= 1).all(axis=1)]
    space = space[(space >= 0).all(axis=1)]
    return space
  def meshgrid(self, x):
    if self.dim <= 2:
      return x
    return np.array(np.meshgrid(x)).flatten()
