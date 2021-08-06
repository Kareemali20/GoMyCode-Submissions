import pandas as pd
import numpy as np

# CREATING EMPTY DICTIONARY
Dict = {

}

# TAKING A NUMBER FROM THE USER
Num = int(input("Please enter a number : "))

for i in range(1,Num + 1):
    Dict[i] = i * i

print(Dict)