# square_root.py
#  for SQUARE ROOT operation.
import math

def square_root(n):
    if n < 0:
        print("\n  Error: Cannot find square root of a negative number!")
    else:
        result = math.sqrt(n)
        print(f"\n  sqrt({n}) = {result}")
