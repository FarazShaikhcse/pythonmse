'''
4. Write a program that receives two numbers from the text fields and calculates the sum and then
displays it in a message box. Generate an exception if the first number is less than the second.
'''
from tkinter import *
from tkinter import messagebox
root = Tk()
def sum():
    a=int(entry1.get())
    b=int(entry2.get())
    if(a>b):
        c=a+b
        messagebox.showinfo("Sum", "sum is "+str(c))
    else:
         messagebox.showerror("Error","Input error")
        
       
L1 = Label(root, text="Enter number1")
L1.pack()    
entry1 = Entry(root)
entry1.pack()
L2 = Label(root, text="Enter number2")
L2.pack()  

entry2 = Entry(root)
entry2.pack()
B1 = Button(root, text = "Sum", command = sum)
B1.pack()
root.mainloop()
