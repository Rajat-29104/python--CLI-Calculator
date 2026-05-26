# logarithm.py
# for LOGARITHM operation.
# log base 10 is the common log.
# log base e  is the natural log (ln).


import math

def logarithm(n):
    if n <= 0:
        print("\n  Error: Log is only defined for positive numbers!")
    else:
        result = math.log10(n)
        print(f"\n  log10({n}) = {result}")

def natural_log(n):
    if n <= 0:
        print("\n  Error: Log is only defined for positive numbers!")
    else:
        result = math.log(n)   
        print(f"\n  ln({n}) = {result}")
