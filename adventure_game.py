def main_hall():
    directions = ["left","right","up","down"]
print("You are in the main hall. There is a thick layer of dust over everything.") 
print("It appears you're all alone, but you spot a table in the corner of the room that looks out of place.")
print("Do you want to go over to the table?")
     
magic_cups = input()
if magic_cups  == "y":
      print("You walk over to it and see a classic three cup magic trick has been set up but you don't see the magician.")
      print("There's a card on the table that says 'Time stands still as do you. Pick up a cup but only 1 and test your luck.")
else:
         print("You've seen too many horror movies and that table looks like a trap. You scan for an exit out of this room")
print("You can go left, right, up or down.Which way would you like to go?")
while userInput not in directions:
    print("Options: left/right/up/down")
    userInput = input()
    if userInput == "left":
      west_wing()
    elif userInput == "right":
      east_wing()
    elif userInput == "up":
      Attic()
    elif userInput == "down":
      Basement()
    else: 
      print("Please enter a valid option.")

# def Attic():
#     directions = ["right","up","down"]
# print("You are in the attic... ") 
# print("It ....")
# print("Do you want to go over to the table?")
     
# qeastion = input()
# if magic_cups  == "y":
#       print("You walk over to it and see a classic three cup magic trick has been set up but you don't see the magician.")
#       print("There's a card on the table that says 'Time stands still as do you. Pick up a cup but only 1 and test your luck.")
#       else magic_cups  == "n":
#       print("You've seen too many horror movies, that table looks like a trap. You scan for an exit out of this room")
# print("You can go left, right, up or down.Which way would you like to go?")
# while userInput not in directions:
#     print("Options: left/right/up/down")
#     userInput = input()
#     if userInput == "left":
#       west_wing()
#     elif userInput == "right":
#       east_wing()
#     elif userInput == "up":
#       Attic()
#     elif userInput == "down":
#       Basement()
#     else: 
#       print("Please enter a valid option.")

def game():

    answer= input("Would you like to play? (y/n)")
    if answer.lower() =='y':
            print("Welcome to the game")
            start=True
            inventory=[]
    else:
            print ("Yeah that's probably for the best... come back when your ready.")
    

game()