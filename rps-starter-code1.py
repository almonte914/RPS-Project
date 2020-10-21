#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
#this allow the use of random.choice#
import random
import os
os.system('clear')


#these are the move selections#
moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""

#Game Players: Player Rock, Random Player, Human Player, Reflective Player, Cycling Player#
#subclass for a player that always plays 'rock'.
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        
        self.my_move = my_move
        self.their_move = their_move
        
#subclass for a player that chooses its moves randomly#    
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)
    
#subclass for human player whose move is chosen by a human#
class HumanPlayer(Player):
    def move(self):
        move = input("\033[97;1;24mWhat is your move? Rock, Paper, Scissors? --> \033[0m")
        while move not in moves:
            move = input("\033[97;1;24mWhat is your move? Rock, Paper, Scissors? --> \033[0m")
        return move 

#subclass for a player that remembers and imitates what the human player did in the previous round.#
class ReflectPlayer(Player):
    def __init__(self):
        self.first_move = random.choice(moves)
        self.their_move = None
    def move(self):
        if self.their_move:
            return self.their_move
        else:
            return self.first_move
    def learn(self,my_move, their_move):
        self.their_move = their_move

#subclass for a player that cycles through the three moves
class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
#this lets the cycleplayer choose a random move for the first round#
        elif self.my_move == None:
            return random.choice(moves)

    def __init__(self):
        super(CyclePlayer, self).__init__()
        self.my_move = None

#Determines Results#
def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

#controls the single round game
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\033[94;1;24mYou played: {move1} \033[0m") 
        print(f"\033[94;1;24mYour opponent played: {move2}\033[0m")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1,move2) is True:
            print("\033[93;1;24mPlayer 1 Wins!\033[0m")
            self.score1 += 1
            print(f"\033[97;1;24mScore: Player1: {self.score1} , Player2: {self.score2} \n\033")
        elif beats(move2, move1) is True:
            print("\033[93;1;24mu'\u2620'Opponent WINS!u'\u2620'\033[0m")
            self.score2 += 1
            print(f"\033[97;1;24mScore: Player1: {self.score1} , Player2: {self.score2} \n\033")
        else:
            print("\033[93;1;24mTIE\033[0m")


 #controls the multiple round game
    def play_game(self):
        
        #Beginning Text#      
        print("\t*****************************************************************************")
        print("\t***  \033[93;1;24mWelcome to My Rock, Paper, Scissors Game I hope you enjoy yourself!\033[0m  ***")
        print("\t*****************************************************************************")
        
        for round in range(1,4):
            print(f"\033[92;1;24mRound {round} : \033[0m")
            self.play_round()
                 
        #Ending Text# 
        print("\033[93;1;24mThank you for Playing, The Game Is Now Over!\033[0m") 

        print(f"\033[97;1;24mFinal Score: Player1: {self.score1} , Player2: {self.score2} \n\033")

        if self.score1 > self.score2:
            print("\033[97;1;24mPLAYER 1 WINS!\033[0m")
        elif self.score1 < self.score2:
            print("\033[97;1;24mu'\u2620'PLAYER 2 WINS!u'\u2620'\033[0m")
        else:
            print("\033[97;1;24mTIE!\033[0m") 

#Method to choose whether to play a single round or several rounds#
if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    #HumanPlayer(), ReflectPlayer()) 
    #RandomPlayer())
    game.play_game()
    #, game.play_round()
