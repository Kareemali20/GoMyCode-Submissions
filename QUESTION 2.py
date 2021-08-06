import numpy as np
import pandas as pd


# FUNCTION FOR CALCULATING THE FACTORIAL USING RECURSION
def Factorial(Num):
    if Num == 0:
        return 1
    else:
        return Num * Factorial(Num - 1)

Number = int(input("Enter the number that you want to get the factorial of it : \n"))
print(Factorial(Number))
