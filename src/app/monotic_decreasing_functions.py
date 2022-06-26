import numpy as np
import re
import math

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
