import pandas as pd
import numpy as np

# CREATING AN EMPTY LIST
List = []

for Num in range(2000,3201):
    if Num % 7 == 0 and Num % 5:
        List.append(Num)

print(List)