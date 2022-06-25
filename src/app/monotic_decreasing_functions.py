import numpy as np
import re

def search_monotic_decreasing_function_subclasses(): 
    return [re.search(r"'app.monotic_decreasing_functions\.(.*)'", str(subclass)).group(1) for subclass in MonoticDecreasingFunction.__subclasses__()]

def monotic_decreasing_function_factory(string):
    return globals()[string]()

class MonoticDecreasingFunction:
    def get_domain(self, points):
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
  def __init__(self):
      self.n = 5
      self.b = np.exp(self.n)
      self.a = 20
  def get_domain(self, points):
    return np.linspace(0, self.a+self.n, points)
  def get_image(self, fs):
    return -np.exp(np.sum(fs, axis=0)-self.a)+self.b

class Cos(MonoticDecreasingFunction):
  def get_domain(self, points):
    return np.linspace(0, np.pi/2, points)
  def get_image(self, fs):
    return np.cos(np.sum(fs, axis=0))

