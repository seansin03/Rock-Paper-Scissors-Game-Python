import random
import sys
from time import sleep
from os import system, name
from typing import final
from termcolor import colored

def greeting():
    """Displays a welcome to the user"""
    user_name = input("Enter Your Name Here: ")
    print(f"Hello " + user_name.title() + " welcome to my game!\nI hope you enjoy")
greeting()


def final_outcome():
    """Final output to run the game"""
    print("Pick one:\nRock = a\nPaper = b\nScissors = c")
    player_selection = input("Enter Selection: ")


    mylist = ["rock", "paper", "scissors"]
    a = mylist[0]
    b= mylist[1]
    c = mylist[2]
    computer_selection = random.choice(mylist)


    if player_selection == "a":
        print("You have entered: Rock")
    elif player_selection == "b":
        print("You have entered: Paper")
    elif player_selection == "c":
        print("You have entered: Scissors")
        
    print(f"Computer has Entered: " + computer_selection)
            

    def rock_output():
        if computer_selection == "rock":
            print(colored("Draw", "blue", attrs=["bold"]))
        elif computer_selection == "paper":
            print(colored("You lost", "red", attrs=["bold"]))
        elif computer_selection == "scissors":
            print(colored("You won", "green", attrs=['bold']))
    


    def paper_output():
        if computer_selection == "paper":
            print(colored("Draw", "blue", attrs=["bold"]))
        elif computer_selection == "scissors":
            print(colored("You lost", "red", attrs=["bold"]))
        elif computer_selection == "rock":
            print(colored("You won", "green", attrs=['bold']))
    


    def scissors_output():
        if computer_selection == "scissors":
            print(colored("Draw", "blue", attrs=["bold"]))
        elif computer_selection == "rock":
            print(colored("You lost", "red", attrs=["bold"]))
        elif computer_selection == "paper":
            print(colored("You won", "green", attrs=['bold']))
    


    if player_selection == "a":
        rock_output()
    elif player_selection == "b":
        paper_output()
    elif player_selection == "c":
        scissors_output()
    
    def clear_screen():
        if name == "nt":
            _ = system('cls')
        else:
            _ = system('clear')
    print('Screen will be cleared') 
    sleep(2)
    clear_screen()

final_outcome()
while True:
    play_again = input("Do you want to play again? Y or N: ")
    if play_again == "y":
        final_outcome()
    elif play_again == "n":
        sys.exit()