import random

# Activity 10.3 Create a function that plays rock paper scissors with you...
# You are to ask to user for input
# If the user inputs "Rock" -> "scissors" will lose, and 'Paper' will win
# If the user inputs 'Paper' -> 'Rock' will lose, and 'Scissor' will win
# If the user inputs 'Scissors' -> 'paper' will lose, and 'Rock' will win

def rockPaperScissors():
  userInput = input("Please take a guess ")
  computerPick = ""
  computerNum = random.randrange(1, 4)

  # Logic for computer taking it's guess
  if(computerNum == 1):
    computerPick = 'rock'
  if(computerNum == 2):
    computerPick = 'paper'
  if(computerNum == 3):
    computerPick = 'scissors'

  # Logic for actually playing
  if(userInput == 'rock' and computerPick == 'paper'):
    print(f"You lose, {computerPick} beats {userInput}")
  elif(userInput == 'paper' and computerPick == 'scissors'):
    print(f'You lose, {computerPick} beat {userInput}')
  elif(userInput == 'scissors' and computerPick == 'rock'):
    print(f'You lose, {computerPick} beats {userInput}')
  elif(userInput == computerPick):
    print("You guessed the same, try again")
  else:
    print(f"You win! {userInput} beats {computerPick}") 

# rockPaperScissors()


def rockPaperScissors2():
  dictOfGuesses = {
    '1' : 'rock',
    '2' : 'paper',
    '3' : 'scissors'
  }
  userInput = input('Input your guess ').lower()
  computerNum = random.randrange(1, 4)
  computerNumToString = str(computerNum)
  computerGuess = dictOfGuesses[computerNumToString]
  # print(computerGuess)
  
  if(userInput == 'rock' and computerGuess == 'paper'):
    print(f"You lose, {computerGuess} beats {userInput}")
  elif(userInput == 'paper' and computerGuess == 'scissors'):
    print(f'You lose, {computerGuess} beats {userInput}')
  elif(userInput == 'scissors' and computerGuess == 'rock'):
    print(f'You lose, {computerGuess} beats {userInput}')
  elif(userInput == computerGuess):
    print("You guessed the same, try again")
  else:
    print(f"You win! {userInput} beats {computerGuess}") 

# rockPaperScissors2()


def iWin():
    pick = input("Choose Rock, Paper, or Scissors")
    pcPicks = ["Rock", "Paper", "Scissors"]
    pcPick = random.choice(pcPicks)
    print(pcPick)
    return pcPick
# iWin() 

def rockPaperScissors3():
  myGuess = input('Input your guess').lower()
  computerOptions = ['rock', 'paper', 'scissors']
  computerGuess = random.choice(computerOptions)

  if(myGuess == 'rock' and computerGuess == 'paper'):
    print(f"You lose, {computerGuess} beats {myGuess}")
  elif(myGuess == 'paper' and computerGuess == 'scissors'):
    print(f'You lose, {computerGuess} beats {myGuess}')
  elif(myGuess == 'scissors' and computerGuess == 'rock'):
    print(f'You lose, {computerGuess} beats {myGuess}')
  elif(myGuess == computerGuess):
    print("You guessed the same, try again")
  else:
    print(f"You win! {myGuess} beats {computerGuess}") 
  # print(computerGuess)

rockPaperScissors3()
