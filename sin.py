# sin.py
#  for SINE operation.
# So first we convert degrees to radians using math.radians().


import math

def sine(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    result = math.sin(angle_in_radians)
    result = round(result, 10)   # fix tiny floating point errors like 1e-16
    print(f"\n  sin({angle_in_degrees}) = {result}")
