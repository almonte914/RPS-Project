#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
#this allow the use of random.choice#
import random

#these are the move selections#
moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""

#Game Players: Player Rock, Random Player, Human Player, Reflective Player, Cycling Player#


print("Hello, Welcome to my version of Rock, Paper, Scissors. I hope you enjoy!")

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        
        self.my_move = my_move
        self.their_move = their_move
        
        
#subclass for computer player who chooses random moves#    
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
#subclass for human player whose move is chosen by a person#

#class HumanPlayer(Player):
#    def move(self):
#        move = input("What is your move? Rock, Paper, Scissors?")
#        return input

#Determines Results#
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        #print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
    
 
    def play_game(self):
        
        #Beginning Text#
        print("The Game Will Now Start!")
        
        
        for round in range(3):
            #print(f"Round {round}:")
            self.play_round()
            
        #Ending Text#    
        print("Thank you for Playing, The Game Is Now Over!")


        #Method to choose whether to play a single round or several rounds#
if __name__ == '__main__':
    game = Game(Player(), RandomPlayer())
    game.play_game()
