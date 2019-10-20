'''
2. (Find the index of the smallest element) Write a function that re
turns the index of the smallest
element in a list of integers. If the number of such elements is greater than 1, return the smallest
index. Use the following header:
def indexOfSmallestElement(lst):
Write a test program that prompts the user to enter a lis
t of numbers, invokes this function to return
the index of the smallest element, and displays the index.
'''
def indexOfSmallestElement(lst):
    return lst.index(min(lst))
l=[]
n=int(input("Enter n")) 
for i in range(n):
    l.append(input("Enter a number"))
print("Index of smallest number is ",indexOfSmallestElement(l))