#Step 2 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)

for _ in range(word_length):
 _ = display.insert(0, "_")
  
user_word_selection = input("Guess a letter associated with the mystery word: ").lower()

print(display)

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

for position in range(word_length):
  letter = chosen_word[position]
  if letter == user_word_selection:
    display[position] = letter
    


#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

print(display)




