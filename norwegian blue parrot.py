# Title: The Norwegian Blue Parrot Guessing Game
# Author: Ryan Heitz (And Zach Theilen is learning!)
# The goal of the game is guess the age of a parrot.
# The program generates a random age between 1 and 20.
# The player gets 5 guesses to guess the age correctly.
# If they're correct, they win the parrot!

import random

# Define artwork
bird_art = """
             _____
          _/       `.
       ,'' . O       \
       
      / ,-. \      '`|_
      |/--._/` _     \ '.
      '   /'-|/ \|`\|-`  \
      
         /   /       \   |
         |  ;    '`  |  .'
         '. |;;      ;  /
          \ \ ;     / ,'
           ;--,   .,--,
        __||=|=|./|=|=||___
          `'-'-'  `-'-'`
  ___________________________
              | |  |
The Norwegian Blue Parrot Guessing Game
              | |  |
              + |  |
              \|\  /
               | ||
               | ||
               | ||
               | ||
               | ||
               \ \/
                ||
                 |
                 |
"""

# Display the title and instructions
print(bird_art)

# Set the scene and give instructions
instructions = """
You walk into an old and smelly pet shop.
As the door closes behind you, you see
a beautiful blue parrot sitting very
still in a cage. The pet shop owner
greets you and says,
"Today is your lucky day!
This is the rare Norwegian Blue parrot.
Guess his age and take him home for free!

You get five guesses.:
"""
print(instructions)

# Making up the parrots age
# Automatically pick a random number between 1 and 20
parrot_age = random.randint(1,20)

number_of_guesses = 0
# While loop will repeat until the number_of_guesses is five
while number_of_guesses < 5:
    # Get a guess from the user
    guess = input("Guess the age of the parrot [number from 1 to 20]: ")
    guess = int(guess)

    # Add one to our guess counter
    number_of_guesses = number_of_guesses + 1

    # Checking to see if the guess is correct
    if guess == parrot_age:
        print("Congratulations! You win! Enjoy your Norwegian Blue!")
        break
    else:
        print("Wrong! You obviously don't know your Norwegian Blues!")

        # Check to see if this is the fifth guess
        # If true, tell them they lost and reveal the parrot's age
        if number_of_guesses == 5:
            print("You lose!")
            print("The Norwegian Blue is " + str(parrot_age))
            
            # Stop Indenting (This marks the end of a while loop)
            
print ("Thank you for playing!")
