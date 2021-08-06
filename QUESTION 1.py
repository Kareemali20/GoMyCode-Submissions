import pandas as pd
import numpy as np

# CREATING AN EMPTY LIST
List = []

#                BEGIN/END
for Num in range(2000,3201):
    # CHECKING THE CONDITION
    if Num % 7 == 0 and Num % 5:
        List.append(Num)

# PRINTING THE NUMBERS IN A LIST
print(List)