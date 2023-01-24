#Challenge 5

import random
from hangman_words import word_list
from hangman_art import stages, logo

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"The word you need to guess is: {display}")    

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"Your letter is '{guess}' and you've already entered it.")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            print(f"Yay, you guessed a letter!! ")

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print(f"Your letter is '{guess}' and it's not in this word. You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("You lost!! Game over!! Try again.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Yay !! You win. What a great game")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])


#Challenge 4

# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
            # display[position] = letter

    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    # print(f"{' '.join(display)}")

    #Check if user has got all letters.
    # if "_" not in display:
    #     end_of_game = True
    #     print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.


#Challenge 3

# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
# display = []
# for _ in range(word_length):
    # display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# end_of_game = False
# while not end_of_game:
#   guess = input("Guess a letter: ").lower()
#Check guessed letter
#   for position in range(word_length):
#     letter = chosen_word[position]
#     print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter == guess:
#       display[position] = letter
#   print(display)
#   if "_" not in display:
#     end_of_game = True
#     print("You win!")


#Challenge 2
# #TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.    
# import random

# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# print(f"The chosen word is {chosen_word}.")

# display = []
# for _ in chosen_word:
#     display += ["_"]
# print(display)    

# guess = input("Guess a letter:\n").lower()

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# word_lenght = len(chosen_word)
# for position in range(word_lenght):
#   letter = chosen_word[position] 
#   if letter == guess:
#     display[position] = letter

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)   


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
