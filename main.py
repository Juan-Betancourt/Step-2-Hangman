#Step 2 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

for letter in chosen_word:
 letter = display.insert(0, "_")
user_word_selection = input("Guess a letter associated with the mystery word: ").lower()

print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

while user_word_selection in chosen_word:
  if user_word_selection == display:
    user_word_selection = display.insert(0, user_word_selection)

def find_number():
    
    for char in chosen_word:
      if char == user_word_selection:
        print("Right")
      else:
        print("Wrong")

find_number()

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.





