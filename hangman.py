#Challenge 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
# print the chosen_word to see if it works corectly :
# print(chosen_word)
print(f"The chosen word is {chosen_word}.")

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

#Challenge 2
# #TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.    

guess = input("Guess a letter:\n").lower()

display = []
for _ in chosen_word:
    display += ["_"]
print(display)    