# Mastermind  Game

import random

def generate_number():
    return str(random.randint(1000, 9999))

def check_guess(secret_number, guess):
    if secret_number == guess:
        return True
    else:
        correct_digits = 0
        for i in range(len(secret_number)):
            if secret_number[i] == guess[i]:
                correct_digits += 1
        return correct_digits

def play_game():
    player1_number = generate_number()
    
    player2_guesses = 0
    while True:
        player2_guess = input("Player 2, enter your guess: ")
        result = check_guess(player1_number, player2_guess)
        
        if result == True:
            print("Player 2 wins! The number was", player1_number)
            break
        else:
            print("Incorrect guess. {} correct digits.".format(result))
            player2_guesses += 1
    
    player2_number = generate_number()
    
    player1_guesses = 0
    while True:
        player1_guess = input("Player 1, enter your guess: ")
        result = check_guess(player2_number, player1_guess)
        
        if result == True:
            print("Player 1 wins! The number was", player2_number)
            break
        else:
            print("Incorrect guess. {} correct digits.".format(result))
            player1_guesses += 1
    
    print("Game Over. Player 1 took", player1_guesses, "guesses. Player 2 took", player2_guesses, "guesses.")

play_game()