import pandas as pd
import numpy as np

# GETTING THE FACTORIAL USING RECURSION
def Factorial (Num):
    if Num == 0 or Num == 1 :
        return 1
    else:
        return Num * Factorial(Num - 1)


# GETTING THE INPUT FROM THE USER
Num = int(input("Please enter a number "))

# CALLING THE FUNCTION
print(Factorial(Num))