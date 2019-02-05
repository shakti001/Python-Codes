#In this section we define dunction for sorting..
def sorting(mylist):
    # In this section we using for loop with range and length.. 
    for i in range(len(mylist)):
        # In this section we using another for loop with length and range..
          for j in range(i+1,len(mylist)):
              # This is  if condition according to question.. 
                   if mylist[i]>mylist[j]:
                        temp=mylist[i]
                        mylist[i]=mylist[j]
                        mylist[j]=temp
    # In this section return mylist..                    
    return mylist
# In this section we define function avg.
def avg(mylist):
    c=1
    s=1
    # In this section we using for loop.. 
    for i in mylist:
        s=s+i
        c=c+1
        # In this section return int.
    return int(s/c)    
# In this section we take input from user.
a=input("enrer num by spaces")     
mylist=list(map(int,a.split()))
 
# In this section we sorted a list..
sorted_list=sorting(mylist)
# this is print section ..
print(sorted_list)
# In this section removing element from '0' index..
mylist.remove(mylist[0])
# In this section removing element from '-1' index..
mylist.remove(mylist[len(mylist)-1])
# This is print section
print("After Ignoring smallest and largest elments from list.The centric average is =",avg(mylist))              
              
    
