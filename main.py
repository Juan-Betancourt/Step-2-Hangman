#Step 1 
import random
word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

user_word_selection = input("Guess a letter associated with the mystery word: ").lower()

def find_number():
    letter_char = []
    
    for char in chosen_word:
      if char == user_word_selection:
        print("Right")
        # letter_char.append(char)
      else:
        print("Wrong")
    # print(letter_char)

find_number()

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
