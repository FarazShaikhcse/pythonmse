'''
3. Write the following function that tests whether the list has four consecutive numbers with the
same value:
def isConsecutiveFour(values):
Write a
test program that prompts the user to enter a series of integers and reports whether the series
contains four consecutive numbers with the same value.
'''
def isConsecutiveFour(values):
    for i in range(len(values)-3):
        if values[i]==values[i+1]==values[i+2]==values[i+3]:
            print("the series contains four consecutive numbers with the same value")
            return
    print("the series doesn't contain four consecutive numbers with the same value")    
l=[]
n=int(input("Enter n:")) 
for i in range(n):
    l.append(input("Enter a number:"))
isConsecutiveFour(l)           