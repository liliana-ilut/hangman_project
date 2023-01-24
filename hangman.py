
#Challenge 2
# #TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.    
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f"The chosen word is {chosen_word}.")

display = []
for _ in chosen_word:
    display += ["_"]
print(display)    

guess = input("Guess a letter:\n").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

word_lenght = len(chosen_word)
for position in range(word_lenght):
  letter = chosen_word[position] 
  if letter == guess:
    display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)   


#Challenge 1 
# import random
# word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# chosen_word = random.choice(word_list)
# print the chosen_word to see if it works corectly :
# print(chosen_word)


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# the code was moved to challenge 2, todo 1
# guess = input("Guess a letter:\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# the code was moved to challenge 2, todo 2

# for letter in chosen_word:
#   if letter == guess:
#     print("right")
#   else:
#     print("wrong")
