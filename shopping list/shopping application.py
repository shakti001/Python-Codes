# Name
# This is a list..
shopping_list = []
#this is print section..
print("what should we pick up at the store ?")
print("Enter 'DONE' to stop adding items,")
while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == 'DONE':
        break
    
    # add new items to our list
    shopping_list.append(new_item)

#  print out the list.
print("Here’s your list")
for item in shopping_list:
    print ( item )
    

# In this section define function for help
def show_help():
    print("current items in the list")
    print("""
Enter 'DONE' to adding to item
Enter 'SHOW' to show your current item
Enter 'HELP' to show your help commands
""")
# In this section define function show list   
def show_list():
    print("Here is your list :")
    # In This section we using for loop..
    for item in shopping_list:
        # this is print section..
        print(item)
# In this section we define function for adding item..
def add_item(new_item):
    # For add item we use '.append' keyword..
    shopping_list.append(new_item)
    print(item)
# In this we call show_help function..
show_help()
# In this we use While True condition ...
while True:
    new_item = input("> ")
    # This is if condition for show 'HELP'.. 
    if new_item == 'HELP':
        show_help()
        continue
    # This is elif condition for upper 'SHOW'..
    elif new_item == 'SHOW':
        show_list()
        continue
    # This is another elif condition for show 'Show'..
    elif new_item == 'Show':
        show_list()
        continue
    # This is another eiif condition for lower 'Show' 
    elif new_item == 'show':
        show_list()
        continue
    add_item(new_item)

show_list()    

