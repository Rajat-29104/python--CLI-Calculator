# divide.py
#  DIVISION operation.(handles divide by zero error).

def divide(a, b):
    if b == 0:
        print("\n  Error: Cannot divide by zero!")
    else:
        result = a / b
        print(f"\n  {a} / {b} = {result}")
