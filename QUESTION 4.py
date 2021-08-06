import numpy as np
import pandas as pd

# FUNCTION FOR CONVERTING STRING TO LIST
def StringToList(String):
    List1=[]
    List1[:0]=String
    return List1

# TAKING THE INDEX AND THE STRING INPUT
String1 = input('Enter a string : \n')
Index = int(input('Enter an index : \n'))

# CONVERTING STRING TO LIST
String2 = StringToList(String1)

# DELETING THE INDEX
del String2[Index]

String2 = "".join(String2)
print(String2)
