from collections import Counter
from math import factorial
from functools import reduce
import operator

def steps(size):
    steps = []
    for i in range(0,size):
        steps.append("x")
        steps.append("y")
    return steps


def unique_permutations(lst):
    c = Counter(lst)
    return factorial(len(lst)) // reduce(operator.mul, map(factorial, c.values()))


print(unique_permutations(steps(20)))