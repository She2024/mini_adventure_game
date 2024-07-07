import time
import datetime
import csv
import json
import os
global score
score = 0

from src.operations import load_score,save_score
from src.game_score import display_score, add_score, high_scoring_game

# This file path works when you run the program from the executable file
FILE_PATH = './data/highest_score_log.json' 
# IF you run just the main.py file from python3 main.py, you fetch the file like this:

def main():
    score = load_score(FILE_PATH)

    if not score:
        print("No scores loaded or an error occured. Exiting.")
        return
    while True:
        print("The score to beat is:")
        print("1. Display scoreboard")
        print("2. Add a new match")
        print("3. Display high-scoring matches")
        print("4: Save and Exit")

        choice = input("Choose an option: ")
 
        if choice == '1':
            score(score)
        elif choice == '2':
            add_score(score)
        elif choice == '3':
            high_scoring = high_scoring(score, 3)
            display_score(high_scoring)
        elif choice == '4':
            try:
                save_score(FILE_PATH, score)
                break
            except Exception as e:
                print(f"Error saving score: {e}")
        else:
            print("Invalid choice, please try again.")  
  

global key

key = False
# Answer question for point
def riddle():
  global score
  print("The riddle is 'I watch you sleep, I haunt you by day. You stare at me and saw nothing, but darkness. What am I?' Enter your answer to escape the room:")
  riddle = "fear" 
  riddle = input()
  if(riddle == "fear"):
            
    print("Correct answer. The librarian steps aside and look for an escape from the library.")
    print("One point awarded")
    score = score + 1
    print(f"{name} current score: {score}")
    library()
  else:
    print("Angered by your incorrect answer she killed you.")
    print(f"{name} current score: {score}")
    
  quit()

# Function for 
def librarian():
  actions = ["answer","flee"]
  print("A librarian appears before you with a riddle, she seems friendly and you have no fear of her. You can answer or flee. What would you like to do?")
  userInput = ""
  while userInput not in actions:
    print("Options: flee/answer")
    userInput = input()
    if userInput == "answer":
       riddle()
    elif userInput == "flee":
      library()
    else:
      print("Invalid option.")

def library():
  directions = ["left","right","up","down"]
  global key
  print("Half the bookshelves are empty and random papers cover the floor. Someone is watching you. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/up/down")
    userInput = input()
    if userInput == "down":
      print("You open the filing cabinet in front of you and among the dusty trinkets and papers you find a key.")
      print("The tag says it's a skeleton key, it must open all the  locks to the building.")
      key = True
      library()
    elif userInput == "left":
      reception()
    elif userInput == "right":
      librarian()
    elif userInput == "up":
      print("Congrats!!. The door opens and you escape the library. Grateful to have found the exit you never want to explore abandoned locations again.")
      print(score)
      quit()  
    else:
      print("Please enter a valid option.")


def coronerOffice():
  directions = ["left","up"]
  print("This is awesome! You find yourself in the coroners office. It still has furniture and files, why would they leave all this behind?")
  print("You hear some scraping sounds but as the sound echoes around the room your not sure where it's coming from. Which direction do you go?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/up")
    userInput = input()
    if userInput == "left":
      print("Your now in the morgue. A showy figure in a medical gown appears before you, like a scene out of '13 Ghosts'.")
      print("You scream and run face first into an open freezer door knocking yourself out. There is no way you're getting out alive.")
      print(f"Bad luck, {name}. Current score: {score}")
      print(score)
      quit()
    elif userInput == "up":
      reception()
    else:
      print("Please enter a valid option.")


def holdingCells():
  global key
  directions = ["down","up"]
  print("You've taken a wrong turn and find yourself in the holding cells. You thought the court room felt bad, this place feels like pure evil.")
  print("The cell door locks behind you and you're confronted with the ghost of notorious cannibal Thomas Jeffrey.")
  print("Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: down/up")
    userInput = input()
    if userInput == "up":
      if key:
        print("Panic floods you and your struggling to think. You use the skeleton key to escape the cell just in time. Congrats!")
        print(f"{name} current score:'{score}")
        courtRoom()   
      else:
        print("This was not the adventure you had in mind. Face to face with pure evil you feel his spectral hand enter your chest and clamp down on your heart. You die.")
        print(score)
      quit()
    elif userInput == "up":
      courtRoom()  
    elif userInput == "down":
      courtRoom()
    else:
      print("Please enter a valid option.")


def courtRoom():
  directions = ["right","up"]
  print("You've enter the old court rooms with beautiful timber furniture and bronze plaques. You can feel the negative energy of the crimes heard here.")
  print("You are creeped out. Where would you like to go?")
  userInput = ""
  while userInput not in directions:
    print("Options: right/left/up")
    userInput = input()
    if userInput == "up":
      holdingCells()
    elif userInput == "left":
      print("You find that this door opens into a wall.")
    elif userInput == "right":
      reception()
    else:
      print("Please enter a valid option.")


def reception():
  directions = ["left","right","down"]
  print("Standing in the main reception area there's nothing much to see. It looks like someone cleared this place out years ago.")
  print("You have to pick a hallway. Which direction do walk?")
  userInput = ""
  while userInput not in directions:
    print("Options: left/right/up/down")
    userInput = input()
    if userInput == "left":
      courtRoom()
    elif userInput == "right":
      library()
    elif userInput == "down":
      coronerOffice()
    elif userInput == "up":
      print("You find that this door opens into a wall.")
    else: 
      print("Please enter a valid option.")


def playGame() :
    score = 0
    
    play = ["yes", "no"]
    print("It's so tempting, do you press a button? Enter yes or no:")
    play = input()           
    if play == "yes":
      guessButton = "b"
      userGuess = ["a","b","c"]
      print("The buttons are flashing randomly.")
      print("The panel says the buttons turn on lights and intercoms and a full system reset but the panel is worn and the button names are gone.")
      time.sleep(1)
      print("It's just too tempting you can't help it you press a button. What button do you press, a, b or c? Enter the letter: ")
      userGuess = input()
      if userGuess == guessButton:
            print(f"Congratulations {name}! You've just turned on the lights to the building. That should help navigate safely… right?")
            print("One point awarded")
            score = score + 1
            print(f"{name} current score: {score}")
            print(score)    
      else:
        print("Too bad! No points awarded")
    else:
        print("You've seen too many horror movies and that table looks like a trap. You scan for an exit out of this room")
    reception()
   


if __name__ == "__main__":
   
    while True:
        print ("Welcome to the Outback Ghost Town.")
        print("There are questions or challenges to complete to obtain points and you navigate through rooms by choosing to walk, left, right, up or down.")
        print("We'll need your name so we can record your score. Please enter your name: ")
        name = input()
        print(f"Good luck, {name}. Score to beat is: No High score recored.")
        print("Camping in the outback you come across an abandoned town.")
        time.sleep (1)
        print("You decide to explore the old government building. It appears to have served a range of services from including the council chambers and the coroners office.")
        time.sleep (1)
        print("Standing at the main reception desk you notice are three buttons labelled A, B, and C. You have no idea what they do.")
        playGame()
       
       
  
 