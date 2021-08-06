import pandas as pd
import numpy as np

C = 50
H = 30

D = [int(x) for x in input("Enter multiple values : \n").split(', ')]

for i in D:
    Formula1 = (2 * C * i)/H
    Formula2 = Formula1 ** 0.5

    print(round(Formula2),end = ' ')
    