# In this section we define add function for sum...
def add(array):
    s=0
    # In this section using for loop ..
    for i in array:
        # this is condition for print sum integer
        s=s+i
        # In this section return s
    return s

# In this section we define mult function for multiply.
def mult(array):
    # this veriable which eqal to 1.
    m=1
    # In this ection using for loop...
    for i in array:
        # This is condition for multuply.
        m=m*i
        # In section return m
    return m

# In this section define function for largest num.
def largest(array):
    # In this section using for loop with length ..
    for i in range(len(array)+1):
        # In this ection we using another loop with range.. 
        for j in range(i+1,len(array)):
            # This is if contdition accroding to question..
            if array[i]<array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    # In this section return array
    return array[0]

# In this section we define function for shortest num. 
def shortest(array):
    # In this section we using for loop with length.
    for i in range(len(array)+1):
        # In this section we using for loop with range..
        for j in range(i+1,len(array)):
            # This is If condition accronding to question..
            if array[i]>array[j]:
                temp=array[i]
                array[i]=array[j]
                array[j]=temp
    # In this ection return '0' index from array..
    return array[0]

# In this section we define function for removing duplicates.. 
def without_duplicate(array):
    # In this we create new list
    new_list=[]
    # In this section we using for loop ..
    for i in array:
        # This is if condition accroding to question with not in operator.
        if i not in new_list:
            # In this section we add element to 'i' index..
            new_list.append(i)
#In this section return new_list..
    return new_list            





# This is array..
array=[5,2,6,2,3]
# This is print section for Given list
print("Given list is=",array)
# This is print section for sum integer..
print("sum of list elements is =",add(array))
# This is print section for multiply int..
print("Multiplication of list elements is =",mult(array))
# This is print section for largest num..
print("Largets no in list is =",largest(array))
# This is print section for shortest num..
print("Shortest no in list is=",shortest(array))
# This is print section for removing duplicates..
print("List elements without duplicate is =",without_duplicate(array))


