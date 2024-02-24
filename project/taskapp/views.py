from django.shortcuts import render
from django.urls import path
import random

def home(request):
    return render(request, 'home.html')

def play(request, choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    winner = determine_winner(choice, computer_choice)
    
    context = {
        'user_choice': choice,
        'computer_choice': computer_choice,
        'winner':winner,
    }
    return render(request, 'play.html', context)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return None  # It's a tie
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 'User'
    else:
        return 'Computer'
