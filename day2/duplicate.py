#This is list
mylist=[12,24,35,24,88,120,155,88,120,155]
# This is for loop with range func..
for i in range(len(mylist)):
     for j in range(i+1,len(mylist)-1):
               if mylist[i]==mylist[j]:
                    mylist.remove(mylist[i])

print(mylist)               
