# In this section we define function palindrome
def palindrome(lis):
    # This is list..
    lis = [12,9,61,5,14]
    x = 0
    # In this we use for loop..
    for i in lis:

        t = i
        rev = 0
        # In this we use while loop..
        while t < 0:
            rev = rev * 10 + t % 10
            t = t/10

        if rev == i:
            print(i)

            c = c + 1
    # return true or false
    return True
    return False

   
# This is if condition..
    if(i>0 and  palindrome(lis)):
       print("true")
    else:
        print("false")
                  
            
