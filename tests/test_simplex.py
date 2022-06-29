import numpy as np
import random
def generate_random_point_on_simplex(dim=3):
    x = []
    rest = 1
    for i in range(0, dim-1):
        x.append(random.random()*rest)
        rest = rest-x[i]
    x.append(rest)
    return np.array(x)

def test_generate_random_point():
    x = generate_random_point_on_simplex()
    assert x.shape[0] == 3
    assert (x>=0).all()
    assert np.sum(x) == 1
