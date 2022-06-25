import numpy as np
import operator
from src.app import ParetoFrontGenerator, Polynomial, Exponential, Sqrt, Cos
maxO = (operator.ge, operator.gt)
minO = (operator.le, operator.lt)
dominates = lambda y, y1, op=minO: np.all(op[0](y,y1)) and np.any(op[1](y,y1))

def find_pareto_given_a_set(A):
  pareto = []
  for y in A:
   if not np.any([dominates(ys, y) for ys in A]):
      pareto.append(y)
  return np.array(pareto).T

def is_a_non_dominated_set(A):
  return np.all(find_pareto_given_a_set(A).T == A)

def setup():
    # This should execute at the start of each test.
    print("Executing Setup")


def teardown():
    # This should execute at the end of each test.
    print("Executing Teardown")

# To test a specific function...
# python -m pytest -s tests/test_nondominated_set_generator.py
def test_generate_nondominated_set_polynomial_dim_n():
    for n in range(2, 50):
          pareto = ParetoFrontGenerator(dim=n, points=100, translation=0)
          space = pareto.generate_space()
          assert space.shape[1] == n and 2 <= space.shape[0] <= 100
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_sqrt_dim_n():
    for n in range(2, 50):
          pareto = ParetoFrontGenerator(dim=n, points=100, translation=0, function=Sqrt())
          space = pareto.generate_space()
          assert space.shape[1] == n and 2 <= space.shape[0] <= 100
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_expontential_dim_n():
    for n in range(2, 15):
          pareto = ParetoFrontGenerator(dim=n, points=100, translation=0, function=Exponential())
          space = pareto.generate_space()
          assert space.shape[1] == n and 2 <= space.shape[0] <= 100
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_cos_dim_n():
    for n in range(2, 5):
          pareto = ParetoFrontGenerator(dim=n, points=100, translation=0, function=Cos())
          space = pareto.generate_space()
          assert space.shape[1] == n and 2 <= space.shape[0] <= 100
          assert is_a_non_dominated_set(space)
