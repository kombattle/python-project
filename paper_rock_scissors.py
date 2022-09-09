# -*- coding: utf-8 -*-
"""paper rock scissors

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fV6nrffrYYPz0TdPvdZ8nAMA3CKa3lqa
"""

def games():
    import random
    win = 0
    lose = 0
    tie = 0
    com_choice = ["rock","paper","scissors"]

    while True:
        user = input("Choose answer: ").lower()
        com = random.choice(com_choice)
        score = (f"Score = Win: {win}, Lose: {lose}, Tie: {tie}")
        
        if user == com:
            print("tie")
            tie =+ 1
            print(score)
        elif user == "rock" and com == "scissors":
            print("win")
            win =+ 1
            print(score)
        elif user == "paper" and com == "rock":
            print("win")
            win =+ 1
            print(score)
        elif user == "scissors" and com == "paper":
            print("win")
            win =+ 1
            print(score)
        elif user == "exit":
            print(f"Your {score}")
            break
        else:
            print("lose")
            lose =+ 1
            print(score)

games()