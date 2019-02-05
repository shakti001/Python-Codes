#This is list which is called mylist..
mylist=[1,3,6,78,35,55]
# This is another list which is called yourlist
yourlist=[12,24,35,24,88,120,155]
# this is a empty list..
intersect_list=[]
print("Mylist is =",mylist)
print("Your List is =",yourlist)
print("intersection of mylist and your list is=")
#This is a for loop..
for i in mylist:
    # This is a another for loop..
    for j in yourlist:
        if i==j:
          intersect_list.append(i)
        
print(intersect_list)      
      
