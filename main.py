#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from random import randint 
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Define turns for each level; easy and hard.
# Global constant
EASY_TURNS = 10
HARD_TURNS = 5

# Create a function to check user’s guess against actual number. 
# Track the number of turns and reduce by 1 if they get it incorrect.
def compare(guess, answer, turns): 
  if answer == guess: 
    print(f"You got it! The answer was {answer}.")
  elif answer > guess: 
    print("Too low.")
    return turns - 1
  elif answer < guess: 
    print("Too high.")
    return turns - 1 

# Create a function to set difficulty.
def difficulty(): 
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_TURNS 
  else: 
    return HARD_TURNS 

# Choose a random number between 1 and 100.
def guess_what():  
  answer = randint(1, 100) 
  
  # Iterate the guessing functionality if they get it incorrect. 
  turns = difficulty()
  guess = 0
  while guess != answer: 
    print(f"You have {turns} attempts remaining to guess the number.") 
    
    # Let the user guess a number.
    guess = int(input("Make a guess:"))

    turns = compare(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer: 
      print("Guess again!")         
   
guess_what()