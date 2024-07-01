### Game intorduction
print("You wake up in the main hall of an abandoned research facsility. You don't know how you got here and you can't remember much about the last few days.") 
print("Panicked you try remember as much as you can. What was I doing last... what year is it... what's my name... OMG what's my name!!") 
print("Okay take a breath I know I have a name so what's my name...") 

### Ask for users name

player_name = input("Please enter your name:")
print(f"{player_name}, my name is {player_name}!!")

## Set the scene
print("There's a thick layer of dust over everything, and it appears you're all alone, but you spot a table in the corner of the room that looks out of place.")
print("Do you want to go over to the table?")

### Ask user to input
magic_cups = input()
if(magic_cups  == "y"):
      print("You walk over to it and see a classic three cup magic trick has been set up but you don't see the magician.")
      print("There's a card on the table that says 'Time stands still as do you. Pick up a cup but only 1 and test your luck.")
      random_number = input():

else:
      print("You've seen too many horror movies and that table looks like a trap. You scan for an exit out of this room")
print("You can go left, right, up or down.Which way would you like to go?")

### Ask player for direction
