"""
Week 4 practice project template for Python Programming Essentials
Rock-paper-scissors-lizard-Spock
"""
import random
from secrets import choice
# the project is saved under:
# https://py3.codeskulptor.org/#user307_Kj9ypN0gVE_1.py


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def name_to_number(name):
    """
    Given string name, return integer 0, 1, 2, 3, or 4 
    corresponding to numbering in video
    """
  
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    pass

    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return "Error: Name does not match!"
    
# print(name_to_number("rock"))		# output - 0
# print(name_to_number("Spock"))		# output - 1
# print(name_to_number("paper"))		# output - 2
# print(name_to_number("lizard"))		# output - 3
# print(name_to_number("scissors"))	# output - 4

#print(name_to_number("rock")==0)		# output - True
#print(name_to_number("Spock")==1)		# output - True
#print(name_to_number("paper")==2)		# output - True
#print(name_to_number("lizard")==3)		# output - True
#print(name_to_number("scissors")==4)	# output - True


"""
Testing template for number_to_name()
"""
def number_to_name(number):
###################################################
# Copy and paste your definition of number_to_name() here
    """
    Given integer number (0, 1, 2, 3, or 4)
    corresponding name from video
    """
    pass
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return "Error: Number does not match!"


###################################################
# Test calls to number_to_name()
# print(number_to_name(0))
# print(number_to_name(1))
# print(number_to_name(2))
# print(number_to_name(3))
# print(number_to_name(4))



###################################################
# Output to the console should have the form:
# rock
# Spock
# paper
# lizard
# scissors
player_count = 0
computer_count = 0
while True:
    def rpsls():
        global player_count , computer_count
        """
        Given string player_choice, play a game of RPSLS 
        and print results to console
        """
        choices = ['rock', 'paper', 'scissors', 'lizard','Spock' ]
    
        # player = player_choice
        player = None
        while player not in choices:
            player = input("'rock', 'paper', 'scissors', 'lizard' or 'Spock'?: ")
        # print a blank line to separate consecutive games
        print("")
        # print out the message for the player's choice
        print("Player's choice:",player)
        # convert the player's choice to player_number using the function name_to_number()
        # print(name_to_number(player))
            
        # compute random guess for comp_number using random.randrange()
        computer = random.choice(choices)    
        # convert comp_number to comp_choice using the function number_to_name()
        number_to_name(computer)
        # print out message for computer's choice
        print("Computer's choice:",computer)
        # print(name_to_number(computer))

        # compute difference of player_number and comp_number modulo five
        
        # use if/elif/else to determine winner and print winner message
        
        
            
        if player == computer:
            print("\ntie\n")
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'rock' and computer == 'paper':
            computer_count  = computer_count + 1
            print("\nComputer wins\n")
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'paper' and computer == 'rock':
            print("\nPlayer wins\n")
            player_count = player_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'paper' and computer == 'Spock':
            print("\nPlayer wins\n")
            player_count = player_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'paper' and computer == 'scissors':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1 
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'paper' and computer == 'lizard':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'rock' and computer == 'lizard':
            print("\nPlayer wins\n")
            player_count = player_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'rock' and computer == 'Spock':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'rock' and computer == 'scissors':
            print("\nPlayer wins\n")
            player_count = player_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'Spock' and computer == 'scissors':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'Spock' and computer == 'lizard':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'lizard' and computer == 'scissors':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'scissors' and computer == 'Spock':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'scissors' and computer == 'paper':
            print("\nPlayer wins\n")
            player_count = player_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'scissors' and computer == 'rock':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'scissors' and computer == 'lizard':
            print("\nPlayer wins\n")
            player_count = player_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'lizard' and computer == 'paper':
            print("\nPlayer wins\n")
            player_count = player_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'lizard' and computer == 'rock':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'lizard' and computer == 'Spock':
            print("\nPlayer wins\n")
            player_count = player_count + 1
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'Spock' and computer == 'paper':
            print("\nComputer wins\n")
            computer_count  = computer_count + 1        
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        elif player == 'Spock' and computer == 'rock':
            print("\nPlayer wins\n")
            player_count = player_count + 1       
            print("Computer count: ", computer_count)
            print("Player count:", player_count)
        pass
    rpsls()
    rpsls()
    rpsls()
    rpsls()
    rpsls()
    play_again = input("Do you want to play again? (yes/no):")

    if play_again != "yes":
        break


    
# test your code
# rpsls()
# rpsls()
# rpsls()
# rpsls()
# rpsls()

# rpsls("rock")
# rpsls("Spock")
# rpsls("paper")
# rpsls("lizard")
# rpsls("scissors")

# always remember to check your completed program against the grading rubric