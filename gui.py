
from tkinter import *
def display():
    var1.set("Name is "+entry1.get())   
    var2.set("Gender is "+rad.get())
    hob=CheckVar1.get()+" "+CheckVar2.get()
    if(hob!=""):
        var3.set("Hobbies are "+hob)
        
root=Tk()
L1 = Label(root, text="Enter name")
L1.pack()    
entry1 = Entry(root)
entry1.pack()
L1 = Label(root, text="Select gender")
L1.pack() 
rad = StringVar()

R1 = Radiobutton(root, text="Male",variable=rad, value="male")
R1.pack()
R2 = Radiobutton(root, text="Female",variable=rad, value="female")
R2.pack()
L4 = Label(root, text="Select hobbies")
L4.pack() 
CheckVar1 = StringVar()
CheckVar2 =StringVar()
C1 =Checkbutton(root, text = "singing", variable = CheckVar1, onvalue = "singing",offvalue = "")
C2 =Checkbutton(root, text = "dancing", variable = CheckVar2, onvalue = "dancing",offvalue = "")

B1=Button(root, text="Submit",command=display)
C1.pack()
C2.pack()
var1 = StringVar()
L2 = Label(root, textvariable=var1)
L2.pack() 
var2 = StringVar()
L3 = Label(root, textvariable=var2)
L3.pack() 
var3 = StringVar()
L5 = Label(root, textvariable=var3)
L5.pack() 
B1.pack()
root.mainloop()