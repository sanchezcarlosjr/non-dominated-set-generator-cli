import numpy as np
from .monotic_decreasing_functions import Polynomial

def normalize_by_l2(matrix):
  return matrix / np.linalg.norm(matrix, axis=-1)[:, np.newaxis]

class ParetoFrontGenerator:
  def __init__(self, dim=2, points=5, translation=0, function=Polynomial()):
    self.dim = dim
    self.points = points
    self.fit_points = points
    self.translation = translation
    self.function = function 
  def search(self):
      while True:
            pareto_front = self.generate_space()
            relative_error = abs(self.points-pareto_front.shape[0])/self.points
            if relative_error <= 0.1:
                return pareto_front
            self.fit_points += 1
  def generate_space(self):
    domain = self.get_domain()
    f = np.append(domain, np.array([self.function.get_image(domain)]), axis=0)
    space= normalize_by_l2(f)
    space = space.T
    space = space+self.translation
    space = space[(space <= 1).all(axis=1)]
    space = space[(space >= 0).all(axis=1)]
    return space
  def get_domain(self):
    domain = np.array(np.meshgrid(*[self.function.get_domain(self.fit_points) for _ in range(0, self.dim-1)]))
    domain = domain.flatten()
    return domain.reshape(self.dim-1, len(domain)//(self.dim-1)) 
