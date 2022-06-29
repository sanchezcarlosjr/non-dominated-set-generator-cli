import numpy as np
import re
import math

def search_monotic_decreasing_function_subclasses(): 
    return [re.search(r"'app.monotic_decreasing_functions\.(.*)'", str(subclass)).group(1) for subclass in MonoticDecreasingFunction.__subclasses__()]

def monotic_decreasing_function_factory(string, dimension, points, *args):
    return globals()[string](dimension, points, *args)


def normalize_by_l2(matrix):
  return matrix / np.linalg.norm(matrix, axis=-1)[:, np.newaxis]

class MonoticDecreasingFunction:
    def __init__(self, dim, points, *args):
        self.dim = dim
        self.fit_points = points
        self.args = args
    def get_space(self):
        domain = np.array(np.meshgrid(*[self.get_domain(self.fit_points) for _ in range(0, self.dim-1)]))
        domain = domain.flatten()
        domain = domain.reshape(self.dim-1, len(domain)//(self.dim-1)) 
        space = np.append(domain, np.array([self.get_image(domain)]), axis=0)
        space = normalize_by_l2(space)
        space = space.T
        return space
    def get_domain(self):
        pass
    def get_image(self, fs):
        pass

class Polynomial(MonoticDecreasingFunction):
  def get_domain(self, points):
    return np.linspace(0, 20, points)
  def get_image(self, fs):
    return np.sum((fs-20)**2, axis=0)

class Sqrt(MonoticDecreasingFunction):
  def get_domain(self, points):
    return np.linspace(0, 10, points)
  def get_image(self, fs):
    return -np.sqrt(np.sum(fs, axis=0))+10

class Exponential(MonoticDecreasingFunction):
  def get_domain(self, points):
    return np.linspace(0, 20, points)
  def get_image(self, fs):
    return -np.exp(np.sum(fs, axis=0)-10)+np.exp(20)

class Cos(MonoticDecreasingFunction):
  def get_domain(self, points):
    return np.linspace(0, 10*np.pi, points)
  def get_image(self, fs):
    return np.cos(np.sum(fs, axis=0)-20)-np.sum(fs, axis=0)+1000

class Erf(MonoticDecreasingFunction):
  def get_domain(self, points):
    return np.linspace(6, 13, points)
  def get_image(self, fs):
      return np.array([-10*math.erf(x-10)+12 for x in np.sum(fs, axis=0)])

class Tan(MonoticDecreasingFunction):
  def get_domain(self, points):
    return np.linspace(0, np.pi/200, points)
  def get_image(self, fs):
    return -np.tan(np.sum(fs, axis=0)-10)+50

class RandomSimplex(MonoticDecreasingFunction):
  def get_space(self):
      return np.array([self.generate_random_point_on_simplex() for _ in range(0, self.fit_points)])
  def generate_random_point_on_simplex(self):
      # https://stackoverflow.com/questions/65154622/sample-uniformly-at-random-from-a-simplex-in-python
      k = np.random.exponential(scale=1.0, size=self.dim)
      return k/sum(k)

class DirichletSimplex(MonoticDecreasingFunction):
  def __init__(self, dim, points, *args):
      super().__init__(dim,points, *args)
      alpha = self.args[0]
      alpha = alpha
      self.alpha = alpha*self.dim if len(alpha) != dim else alpha
  def get_space(self):
    return np.array([self.generate_random_point_on_simplex() for _ in range(0, self.fit_points)])
  def generate_random_point_on_simplex(self):
      # https://math.stackexchange.com/questions/32618/uniform-distribution-on-a-simplex-via-i-i-d-random-variables
      return np.random.dirichlet(alpha=self.alpha, size=self.dim)


