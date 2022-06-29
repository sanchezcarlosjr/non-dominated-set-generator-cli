import numpy as np
import operator
from src.app import *
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
    for n in range(2, 4):
          pareto = ParetoFrontGenerator(function=Polynomial(dim=n, points=10))
          space = pareto.generate_space()
          assert space.shape[1] == n and 10 <= space.shape[0]
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_sqrt_dim_n():
    for n in range(2, 4):
          pareto = ParetoFrontGenerator(function=Sqrt(dim=n, points=10))
          space = pareto.generate_space()
          assert space.shape[1] == n and 10 <= space.shape[0] 
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_expontential_dim_n():
    for n in range(2, 4):
          pareto = ParetoFrontGenerator(function=Exponential(dim=n, points=10))
          space = pareto.generate_space()
          assert space.shape[1] == n and 10 <= space.shape[0]
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_cos_dim_n():
    for n in range(2, 4):
          pareto = ParetoFrontGenerator(function=Cos(dim=n, points=10))
          space = pareto.generate_space()
          assert space.shape[1] == n and 10 <= space.shape[0]
 
def test_generate_nondominated_set_erf_dim_n():
    for n in range(2, 3):
          pareto = ParetoFrontGenerator(function=Erf(dim=n, points=10))
          space = pareto.generate_space()
          assert space.shape[1] == n and 10 <= space.shape[0]
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_tan_dim_n():
    for n in range(2, 4):
          pareto = ParetoFrontGenerator(function=Tan(dim=n, points=10))
          space = pareto.generate_space()
          assert space.shape[1] == n and 10 <= space.shape[0]
          assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_random_simplex_dim_n():
    for n in range(2, 20):
         pareto = ParetoFrontGenerator(function=RandomSimplex(dim=n, points=50))
         space = pareto.generate_space()
         assert space.shape[1] == n and space.shape[0] == 50
         assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_dirichlet_simplex_dim_n():
    for n in range(2, 20):
         pareto = ParetoFrontGenerator(function=DirichletSimplex(n, 10, [1]))
         space = pareto.generate_space()
         assert space.shape[1] == n and space.shape[0] >= 10
         assert is_a_non_dominated_set(space)


