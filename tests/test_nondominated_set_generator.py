import numpy as np
import operator
from src.app import ParetoFrontGenerator
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
def test_generate_nondominated_set_polynomial_dim2():
    pareto = ParetoFrontGenerator(dim=2, points=60, translation=0.7)
    space = pareto.generate_space()
    assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_polynomial_dim3():
    pareto = ParetoFrontGenerator(dim=3, points=60, translation=0.7)
    space = pareto.generate_space()
    assert is_a_non_dominated_set(space)

def test_generate_nondominated_set_polynomial_dim2_and_it_translates():
    pareto = ParetoFrontGenerator(dim=2, points=60, translation=0)
    space = pareto.generate_space()
    assert is_a_non_dominated_set(space)
