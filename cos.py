# cos.py
# COSINE operation.

import math

def cosine(angle_in_degrees):
    angle_in_radians = math.radians(angle_in_degrees)
    result = math.cos(angle_in_radians)
    result = round(result, 10)
    print(f"\n  cos({angle_in_degrees}) = {result}")
