import random
import time
from typing import final
from termcolor import colored

def greeting():
    """Displays a welcome to the user"""
    user_name = input("Enter Your Name Here: ")
    print(f"Hello " + user_name.title() + " welcome to my game!\nI hope you enjoy")
greeting()

while True: 
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
        
    final_outcome()



