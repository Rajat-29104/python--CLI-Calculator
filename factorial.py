# factorial.py
# FACTORIAL operation.
# Factorial means: n! = n x (n-1) x (n-2) x ... x 1

import math

def factorial(n):
    # n must be a whole number (not 5.5 or negative)
    if n < 0:
        print("\n  Error: Factorial not defined for negative numbers!")
    elif not float(n).is_integer():
        print("\n  Error: Factorial only works for whole numbers!")
    else:
        n = int(n)
        result = math.factorial(n)
        print(f"\n  {n}! = {result}")
