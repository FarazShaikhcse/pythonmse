''''1.
(Display matrix of 0s and 1s) Write a function that displays an n by n matrix using the
following header:
def printMatrix
(n):
Each element is 0 or 1, which is generated randomly. Write a test program that prompts the
user to enter n and displays an n by n matrix.
Sample run:
Enter n: 3
0 1 0
0 0 0
1 1 1
'''


import random
from random import randint
def printMatrix(n):
    for i in range(n):
        for j in range(n):
            print(randint(0,1),end=" ")
        print()  

n=int(input("Enter n:")) 
print("The random matrix is")       
printMatrix(n)          
