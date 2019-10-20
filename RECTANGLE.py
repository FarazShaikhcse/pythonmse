class rectangle:
    def __init__(self,w,h):
        self.w=w
        self.h=h
    def getarea(self):
         return self.w*self.h
n=int(input("Enter the number of rectangles"))        
r=[]  
a=[]
for i in range(n):
    w=int(input("Enter the width of rectangle"+str(i+1)))
    h=int(input("Enter the height of rectangle"+str(i+1)))
    r.append(rectangle(w,h))
    a.append(r[i].getarea())
    print("Area of rectangle %d is %d"%(i+1,r[i].getarea()))
s=a.index(min(a))
print("width of smallest rect",r[s].w)
print("height of smallest rect",r[s].h)
l=a.index(max(a))
print("width of largest rect",r[l].w)
print("height of largest rect",r[l].h)
