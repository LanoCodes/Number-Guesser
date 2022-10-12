from art import logo
import random

print(logo)

print("Welcome to Number Guesser! A game where you try to guess my number!")
print("I'm thinking of a number between 1 and 100...")
NUMBER_TO_GUESS = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def guesser():
  global NUMBER_TO_GUESS
  tries = 10
  if difficulty == 'easy':
    while tries != 0:
      if tries > 1:
        print(f"You have {tries} tries left to guess the number: ")
      else:
        print(f"You have {tries} try left... no pressure: ")
  
      user_guess = int(input("Make a guess: "))
      if user_guess > NUMBER_TO_GUESS:
        print("Too High.")
      elif user_guess < NUMBER_TO_GUESS:
        print("Too Low.\n")
      else:
        print(f"You got it! The answer was {NUMBER_TO_GUESS}")
        return True
      
      tries -= 1
  elif difficulty == 'hard':
    tries = 5
    while tries != 0:
      if tries > 1:
        print(f"You have {tries} tries left to guess the number: ")
      else:
        print(f"You have {tries} try left... no pressure: ")
  
      user_guess = int(input("Make a guess: "))
      if user_guess > NUMBER_TO_GUESS:
        print("Too High.\nGuess again.")
      elif user_guess < NUMBER_TO_GUESS:
        print("Too Low.\nGuess again.")
      else:
        print(f"You got it! My number was {NUMBER_TO_GUESS}")
        return True
        
      tries -= 1

if guesser() != True:
  print(f"You've run out of guesses, you lose..\nMy number was actually {NUMBER_TO_GUESS}")