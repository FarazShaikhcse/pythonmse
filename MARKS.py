marks={'John':86.5,'Jack':91.2,'Jill':84.5,'Harry':72.1,'Joe':80.5}
sorted_list=sorted(marks,key=marks.get,reverse=True)
print("Top3students")
for j in sorted_list[:3]:
    print(j,":",marks[j])
sum1=0
for i in marks:
     sum1+=marks[i]
avg=sum1/5
print("Average=",str(avg))