# In this we are call a random module ..
import random
# In this section we define a function ..
def welcome():
    # In this section we are take input from user
    name = input("ENTER YOUR NAME: ")
    # This is print section
    print("welcome", name)
    print("_","_","_","_","_")
    print("TRY TO GUESS THE WORD IN 5 TRIES OR LESS")
    hangman()
   


# In this section we define another function hangman..
def hangman():
    # In this we use choice random fruits
    
    word = random.choice(["banana", "apple", "orange",])


    # In this we use letters for selection fruits..
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    turns = 8

    guessed = ''
    # This is while loop with len of word
    while len(word) > 0:
        msg = ""
        missed = 0
        # This is for loop ..
        for letter in word:
            # This is if condition for guessed..
            if letter in guessed:
                msg = msg + letter
                # This is else condition..
            else:
                msg = msg + "_" + " "
                missed += 1


           # This is another if codition..
            if msg == word:
                # This is print section..
                print(msg)
                print("you are win, the word was :",word)
                break
            print("guess the word :", msg)
            guess = input()

           # In this if condition we guess in letters
            if guess in letters:
                guessed = guessed + guess
            # This is else condition..
            else:
                print("ENTER A VALID LETTER: ")

                guess = input()
           # In this this if condition guess not in word..
            if guess not in word:
                # your selection is wrong turn will be decresed..
                turns = turns - 1
                if turns == 7:
                    print("your left turn is 7.")
                if turns == 6:
                    print("your left turn is 6.")
                if turns == 5:
                    print("your left turn is 5.")
                if turns == 4:
                    print("your left turn is 4.")
                
                if turns == 3:
                    print("your left turn is 3.")   
                   
                if turns == 2:
                    print("your left turn is 2.")
                if turns == 1:
                    print("sorry your loss.",word)


# Calling welcome function..
welcome()
 


         

            
