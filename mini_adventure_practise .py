# import time

# score = 0
# bonus = 0




# ### Game introduction
# print("You wake up in the main hall of an abandoned research facility. You don't know how you got here and you can't remember much about the last few days.") 
# time.sleep(3)
# print("Panicked you try remember as much as you can. What was I doing last... what year is it... what's my name... OMG what's my name!!") 
# time.sleep(3)
# print("Okay take a breath I know I have a name so what's my name...") 

# ### Ask for users name

# player_name = input("Please enter your name:")
# print(f"What's my name... Oh'{player_name}, my name is {player_name}!!'")

# ## Set the scene
# print("There's a thick layer of dust over everything, and it appears you're all alone, but you spot a table in the corner of the room that looks out of place.")
# time.sleep(3)
# print("Do you want to go over to the table? Enter yes or no: ")

# ### Ask user to input
# magic_cups = input()
# if(magic_cups  == "yes"):
#       print("You walk over to it and see a classic three cup magic trick has been set up but you don't see the magician.")
#       time.sleep(3)
#       print("There's a card on the table that says 'Time stands still as do you. Pick up a cup but only 1 and test your luck.")
      
#       guess_num = 3
#       user_guess = None
#       user_guess = int(input("What's your guess cup, 1, 2 or 3)? Enter the number: "))

#       if user_guess == guess_num:
#          print(f"Congratulations {player_name}! You've just found a single use key that can be used to get you out of danger, use it wisely")
#          bonus += 1
#          ## add code for bonus point tracker
#       else:
#           print("Too bad! No bouns awarded")

# else:
#       print("You've seen too many horror movies and that table looks like a trap. You scan for an exit out of this room")
#       time.sleep(3)
#       print("You can go left to the West wing, right to the east wing, up to the attic or down to the basement. Which room you like to go to?")

# ### Ask player for direction
# roomChoice = input("")
# labChoice = input("")
# riddle = "fear"
# useBonus = input("")

# if(roomChoice == "west wing"):
#      print("You go to the west wing.")
#      print("There is a collection scary looking medical devices and beakers of different coloured fluids in this room.")
#      time.sleep(3)
#      print("You have no trouble imagining Dr Jekyll or Dr Frankenstein working in this lab.")
#      time.sleep(3)
#      print("Suddenly the door behind you closes a faint click of lock engaging is heard! To open the door and return to  the main hall you must correctly answer a riddle.")
#      time.sleep(3)
#      print("You look around the room and see there is a second door, you don't know where it leads or what danger lays in wait.")
#      print("Do you want to go through the door and deeper into the lab? Enter yes or no: ")
     
#      if(labChoice == "yes"):

#         print("Oh no you've fallen for their trap. You entered a red room with no windows or alternative exit.") 
#         ## Add code - If bonus point return to west wing
#         print("The door automatically closes and there is no escape.")
#         time.sleep(3)
#         print("You can't breath and panic grips you. You lose consciousness as the sound of bone saw whirs to life.")
#         time.sleep(3)
#         print(f"Game Over. Better luck next time {player_name}.")
#      else:
#         print(f"Smart move {player_name}, who know what horrors are hidden behind that door.")
#         time.sleep(3)
#         print("You head over to the main door and read the instruction. To open the locked door, you must correctly answer a riddle. Hmm can't be too hard, can it?")
#         time.sleep(2)
#         print("The riddle is 'I watch you sleep, I haunt you by day. You stare at me and saw nothing, but darkness. What am I?' Enter your answer to escape the room:")
#      if(riddle == "fear"):
#          print("Correct answer. The door opens and you escape the west wing. This place is creepy and you're more determined than ever to find your way out.")
#          ## Option to use bonus point to escape room
#      elif((riddle != "fear")+ bonus > 0):
#           print("Incorrect answer. Would you like to use your bonus point to escape the room? Enter yes or no")
        
      
# elif(roomChoice == "east wing"):
#      print("You go to the east wing.")
#      print("It looks like an old kitchen and dining space.")
      
# elif(roomChoice == "attic"):
#      print("You go to the attic.")
#      print("")
      
# elif(roomChoice == "basement"):
#      print("You go to the basement.")
#      print("")
      
# else:    
#     print("Invalid choice. Please enter west wing, east wing, attic or basement")
