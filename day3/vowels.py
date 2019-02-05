# In this we create list..
mylist = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
# This is vowels..
vowels = ('a','A','e','i','o','u','I','U','O','E')
# This update list which is empty..
update_list=[]
# This is for loop
for i in range(len(mylist)):
    for j in mylist[i]:
        if j not in vowels:
            update_list.append(j)
print(update_list)        
    
    
        
            
    
    
