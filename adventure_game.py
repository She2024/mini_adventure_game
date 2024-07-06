import time

global score


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
    print("Options: left/right/up/forward")
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
            print(f"{name} current score:")
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
       
       
    
