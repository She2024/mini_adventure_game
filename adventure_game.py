import time


def playGame() :
    input = ["yes", "no"]
    play = input()           
    if play == "yes":
      guessButton = "b"
      userGuess = ["a","b","c"]
      print("The buttons are flashing randomly. The instructions say 'Only 1 button can be pressed before a full system reset is required.")
      time.sleep(3)
      print("It's just too tempting you can't help it you press a button")
      userGuess = int(input("What button do you press, a, b or c?)? Enter the letter: "))
      if userGuess == guessButton:
        print(f"Congratulations {name}! You've just turned on the lights to the building. That should help navigate safely… right?")
        print("One point awarded")
        bonus += 1
        #add in code to collect score
      else:
        print("Too bad! No points awarded")
    else:
     print("You've seen too many horror movies and that table looks like a trap. You scan for an exit out of this room")
    #reception()
    quit()


if __name__ == "__main__":
    while True:
        print ("Welcome to the Outback Ghost Town.")
        print("There are questions or challenges to complete to obtain points and you navigate through rooms by choosing to walk, left, right, up or down.")
        print("We'll need your name so we can record your score. Please enter your name: ")
        name = input()
        print(f"Good luck, {name}. Score to beat is: No High score recored.")
        print("Camping in the outback you come across an abandoned town.")
        time.sleep (3)
        print("You decide to explore the old government building. It appears to have served a range of services from including the council chambers and the coroners office.")
        time.sleep (4)
        print("Standing at the main reception desk you notice are three buttons labelled A, B, and C. You have no idea what they do.")
        time.sleep (3)
        print("It's so tempting you really want to press a button")
        playGame()
        #quit()
        
