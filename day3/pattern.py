# In this section we take integer input from user..
row=int(input("enter no of rows"))
# This is for loop..
for i in range(1,row+1):
  for j in range(1,i+1):
      print("*", end="")
  print()    

for k in range(row+1,0,-1):
  for l in range(k+1,1,-1):
      print("*",end="")
  print()    
        
        

        
