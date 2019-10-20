
from tkinter import *
from tkinter import messagebox
def sum():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a+b
    messagebox.showinfo("Sum", "sum is "+str(c))
def sub():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a-b
    messagebox.showinfo("Difference", "difference is "+str(c))    
def mul():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a*b
    messagebox.showinfo("Multiplication", "Product is "+str(c))      
def div():
    a=int(entry1.get())
    b=int(entry2.get())
    c=a/b
    messagebox.showinfo("Division", "quotient is "+str(c))          
root=Tk()
L1 = Label(root, text="Enter input 1")
L1.pack()    
entry1 = Entry(root)
entry1.pack()
L2 = Label(root, text="Enter input 2")
L2.pack()    
entry2 = Entry(root)
entry2.pack()
B1 = Button(root, text = "add", command = sum)
B1.pack()
B2 = Button(root, text = "sub", command = sub)
B2.pack()
B3 = Button(root, text = "mul", command = mul)
B3.pack()
B4 = Button(root, text = "div", command = div)
B4.pack()
root.mainloop()