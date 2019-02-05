# In this section create string ..
mystring="python 3.6"
# In this section we count letters..
letters_count=0
# In this section we count digits..
digits_count=0
# This is for loop... 
for i in mystring:
    # This is if condition for count letters..
    if i.isalpha():
        letters_count += 1
        # This is if condition for count digits
    if i.isdigit():
        digits_count += 1
# This is print section for my string.. 
print("My String is =",mystring)
# This is print section for letters..
print("Number of letters in mystring is =",letters_count)
# This is print section for digits..
print("Number of digits in mystring is =",digits_count)
