import time
Bonus = False
bonus = 0
name = input()

## Main Hall

def mainHall():
  directions1 = ["left", "right", "up", "down"]
  print("There's a thick layer of dust over everything. There is a vacant reception desk with out date equipment and an empty phamlet stand.")
  time.sleep(5)
  print("You can go left to the west wing, right to the east wing, up to the attic or down to the basement. Which room you like to go to?")
  userInput =("")
  while userInput not in directions1:
    print("Options: left/right/up/down")
    userInput = input()
    if userInput == "left":
      westWing()
    # elif userInput == "right":
    #   eastWing()
    # elif userInput == "up":
    #   attic()
    # elif userInput == "down":
    #   basement()
    else: 
      print("Please enter a valid option.")

## West Wing

def westWing():
  print("You're in the west wing.")
  print("There is a collection scary looking medical devices and beakers of different coloured fluids in this room.")
  time.sleep(5)
  print("You have no trouble imagining Dr Jekyll or Dr Frankenstein working in this lab.")
  time.sleep(5)
  print("Suddenly the door behind you closes a faint click of lock engaging is heard! To open the door and return to  the main hall you must correctly answer a riddle.")
  time.sleep(5)
  print("You look around the room and see there is a second door, you don't know where it leads or what danger lays in wait. Do you want to go through the door and deeper into the lab? Enter yes or no: ")
  
labChoice = ["yes", "no"]
userInput =("")
riddle = "fear"  
labChoice = input()
if labChoice == "yes":
     print("Oh no you've fallen for their trap. You entered a red room with no windows or alternative exit.")
     print("The door automatically closes and there is no escape.")
     time.sleep(5)
     print("You can't breath and panic grips you. You lose consciousness as the sound of bone saw whirs to life.")
     time.sleep(5)
     print(f"Game Over. Better luck next time {name}.")
else:
   print(f"Smart move {name}, who know what horrors are hidden behind that door.")
   time.sleep(5)
   print("You head over to the main door and read the instruction. To open the locked door, you must correctly answer a riddle. Hmm can't be too hard, can it?")
   time.sleep(5)
   print("The riddle is 'I watch you sleep, I haunt you by day. You stare at me and saw nothing, but darkness. What am I?' Enter your answer to escape the room:")
if(riddle == "fear"):
    print("Correct answer. The door opens and you escape the west wing. This place is creepy and you're more determined than ever to find your way out.")
    ## Option to use bonus point to escape room
elif((riddle != "fear")+ bonus > 0):
    print("Incorrect answer. Would you like to use your bonus point to escape the room? Enter yes or no")
directions2 = ["right", "up"]
while userInput not in directions2:
    print("Options: right/up/")
    userInput = input()
    if userInput == "left":
      westWing()
    # elif userInput == "right":
    #   eastWing()
    # elif userInput == "up":
    #   attic()
    # elif userInput == "down":
    #   basement()
    else: 
      print("Please enter a valid option.")

# Game intorduction and ask for player name
if __name__  == "__main__":

  while True:
    print("You wake up on the floor main hall of an abandoned hospital. You don't know how you got here and you can't remember much about the last few days.")  
    time.sleep(5)
    print("Panicked you try remember as much as you can. What was I doing last... what year is it... what's my name... OMG what's my name!!")  
    time.sleep(5)
    print("Okay take a breath I know I have a name so what's my name...")
    print("Enter name:")
    print(f"What's may name... oh! My name is {name}!!")
    print("It appears you're all alone, you spot a table in the corner of the room that looks out of place.")
    time.sleep(5)
    print("Do you want to go over to the table? Enter yes or no: ")
    playGame = input() 
        
    if playGame == "yes":
      guessNum = 3
      userGuess = None
      print("There's a card on the table that says 'Time stands still as do you. Pick up a cup but only 1 and test your luck.")
      userGuess = int(input("What's your guess cup, 1, 2 or 3)? Enter the number: "))
      if userGuess == guessNum:
        print(f"Congratulations {name}! You've just found a bonus point that can be used to get you out of danger, use it wisely")
        bonus += 1
        #add in code to collect bonus
      else:
        print("Too bad! No bonus awarded")
    else:
     print("You've seen too many horror movies and that table looks like a trap. You scan for an exit out of this room")
     
mainHall()

quit()

