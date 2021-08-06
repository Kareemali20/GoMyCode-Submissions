import pandas as pd
import numpy as np

# ASKING THE USER IF HE WANTS 1 OR 2 DIMENSIONAL ARRAY
Choice = int(input("Do you want 1 or 2 dimension array ?"))

Array1 = []
Array2 = []

if Choice == 1:
    Elem = int(input('Enter the number of elements you want in the arrays : '))
    Array1 = np.random.randint(1, 50, size = Elem)
    Array2 = np.random.randint(1, 50, size = Elem)
elif Choice == 2:
    Rows = int(input('Enter the number of Rows : '))
    Columns = int(input('Enter the number of Columns : '))
    Array1 = np.random.randint(1, 50, size = (Rows,Columns))
    Array2 = np.random.randint(1, 50, size = (Rows,Columns))
elif Choice != 1 and Choice !=2:
    print("WRONG CHOICE !")

print(f'Covariance matrix of the said arrays : \n {np.cov(Array1, Array2)}')