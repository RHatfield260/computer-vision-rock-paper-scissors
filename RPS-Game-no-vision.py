import random as rd
from pick import pick
import numpy as np
choices = ['Rock','Paper','Scissors']
def get_computer_choice():
    computer_choice = rd.choice(choices)
    return computer_choice
def get_user_choice():
    input_message = ('Select Rock, Paper or Scissors!')
    user_choice, index = pick(choices,input_message, indicator = '->',default_index = 0)
    return user_choice
def get_winner(computer_choice,user_choice):
    if user_choice == computer_choice:
        print('Draw')
    elif (user_choice == 'Rock' and computer_choice == "Scissors") or (user_choice == "Paper" and computer_choice == "Rock") or (user_choice == 'Scissors' and computer_choice =='Paper'):
        print('You Win!')
    else:
        print('You Lose!')
def play():
    get_computer_choice()
    get_user_choice()
    get_winner(get_computer_choice(),get_user_choice())   
play()

