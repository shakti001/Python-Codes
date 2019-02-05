
def Addition(mylist):
    s=0
    for i in mylist:
        return i   




x=input("Enter Elements")
mylist=list(map(int,x.split()))
print("list is",mylist)
n=len(mylist)
for i in range(0,n):
    for j in range(i+1,n-1):
        if mylist[i]==13:
            mylist.remove(mylist[j])
            n=n-1
            
    n=n-1   
        
print(mylist)
print("Sum of elements is =",Addition(mylist))

            
    
                
