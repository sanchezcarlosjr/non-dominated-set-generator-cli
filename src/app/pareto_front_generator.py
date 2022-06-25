import numpy as np
import random

def normalize_by_l2(matrix):
  return matrix / np.linalg.norm(matrix, axis=-1)[:, np.newaxis]

def polynomial(fs):
  return np.sum((fs-10)**2, axis=0)

class ParetoFrontGenerator:
  def __init__(self, dim=2, points=5, translation=0):
    self.dim = dim
    self.points = points
    self.translation = np.array([translation]).T
  def generate_space(self):
    fs = []
    for n in range(0, self.dim-1):
      fs.append(self.meshgrid(np.linspace(-20, 10, self.points)))
    fs.append(polynomial(np.array(fs)))
    fs = np.array(fs)
    space = normalize_by_l2(fs)
    space = space+self.translation
    space = space.T
    space = space[(space <= 1).all(axis=1)]
    space = space[(space >= 0).all(axis=1)]
    return space
  def meshgrid(self, x):
    if self.dim <= 2:
      return x
    return np.array(np.meshgrid(x)).flatten()
