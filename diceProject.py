import random
#imports the random number library
rolls = int(input("How many times do you want to roll?"))
#Asks the user for number of dice rolls and converts that string to an integer
diceType =int( input("How many sides do you want your dice to have?"))
#asks the user for number of sides on the dice roll and converts the string to an integer
for rollz in range (rolls):
    #creates the loop within the amount of rolls set by the user
    randomDice = random.randrange(diceType)+1
    #ensures the rolls are to the specifications of the user
    print ("Your roll was:")
    print (randomDice)
    #prints the outputs of the dice rolls
    if diceType == 20:
        #checks if the dice has 20 sides
        if randomDice==20:
            print("Critical hit!")
            #checks if the 20 sided dice roll was a 20
        elif randomDice==1:
            print("Critical Failure")
            #checks if the 20 sided dice roll was a 1

#       I used the int functon from https://www.geeksforgeeks.org/python-int-function/
#       https://github.com/adk7994/Dice-Roller
