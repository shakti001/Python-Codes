# In this section we using veriable mystring..
mystring="www.google.com"
# This is empty dictonary..
mydict={}
# In this section we using for loop..
for i in mystring:
    # This is if condition accroding to question..
    if i in mydict:
        mydict[i] += 1
        # this else condition..
    else:
        mydict[i]=1
# This is print section..
print(str(mydict))        
        
