# Dice Poker
 
from random import *
 
class DicePoker:
 
    def __init__(self):
        self.initialMoney = 100
        self.money = self.initialMoney
        self.dice  = Dice()
        self.UI    = UserInterface()
        self.buyin = 10
 
 
    def increaseMoney(self, val):
        self.money += val
 
    def decreaseMoney(self, val):
        self.money -= val
 
    def playRound(self):
        try:
            self.decreaseMoney(self.buyin)
            self.UI.displayMoney(self.money)
 
            self.dice.roll([1,2,3,4,5]) # this rolls all the dice
            self.UI.displayDice(self.dice.getState())
 
            # Now do two enhancements
            for enhancement in range(2):
                reRollList = self.UI.reRollQuestion()
                self.dice.roll(reRollList)
                self.UI.displayDice(self.dice.getState())
 
            handName, handScore = self.dice.score()
            self.increaseMoney(handScore)
            self.UI.displayMoney(self.money)
            self.UI.displayDice(self.dice.getState())
            self.UI.displayHand(handName)

        except IndexError:
            print( "Please enter yes or no!")
        except ValueError:
            print("Please enter a number from 1 to 5")
    def playGame(self):
 
        self.UI.printIntro()
        while True:
            if self.UI.newRoundQuestion() == False:
                self.UI.displayMoney(self.money)
                break
 
            self.playRound()
             
            if self.money < self.buyin:
                self.UI.displayMoney(self.money)
                response = self.UI.newGameQuestion()
                if response == True:
                    self.money = self.initialMoney
                else:
                    break
 
 
class Dice:
 
    def __init__(self):
        self.state = [1,1,1,1,1]
        self.sides = 6
 
    def roll(self, positions):
        '''
        Input: positions is a list of dice positions
        to roll, numbered 1 to 5.
        '''
        for pos in positions:
            self.state[pos-1] = randint(1,6)
 
    def getState(self):
        return self.state
 
    def score(self):
        'Return: string name of hand, then monetary value'
        D = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        for x in self.state:
            D[x] = D[x] + 1
 
        values = list(D.values())
        if 5 in values:
            handName = 'five of a kind'
            handScore = 30
        elif 4 in values:
            handName = 'four of a kind'
            handScore = 15
        elif 3 in values and 2 in values:
            handName = 'full house'
            handScore = 12
        elif 3 in values:
            handName = 'three of a kind'
            handScore = 8
        elif values.count(2) == 2:
            handName = 'two pairs'
            handScore = 5
        elif values.count(1) == 5 and (D[1] == 0 or D[6] == 0):
            handName = 'straight'
            handScore = 20
        else: 
            handName = 'garbage'
            handScore = 0
 
             
        return handName, handScore 
 
 
class UserInterface:
 
    # TEMPORARY INTRO
    def printIntro(self):
        print("Welcome to Dice Poker! You start with $100. Each round/game costs $10 to play.\n"
              "The scores are as follows:"
              "\nTwo Pairs: $5\nThree of a kind: $8\nFull House(A Pair and a Three of a kind):$12"
              "\nFour of a kind: $15\nStraight(1-5 or 2-6): $20\nFive of a kind: $30\n")
 
    def displayMoney(self, val):
        print("Amount of money: ", val)
 
    def newRoundQuestion(self):
        'Returns True to keep playing, False to stop'
        playAgain = input("Play a round? (yes or no): ")
        playAgain = playAgain.lower()
        return (playAgain[0] == 'y')
    
 
        
        
 
    def displayDice(self, diceList):
        print("Dice are: ", diceList)
 
    def displayHand(self, handName):
        print("Your hand: ", handName)
 
    def reRollQuestion(self):
        reRollList = []
        while True:
            user = input("Give me a die to re-roll (enter when done): ")
            if user == '':
                break
            reRollList.append(int(user))
 
        return reRollList
 
    def newGameQuestion(self):
        'Return True for play again, False for not'
        
        playAgain = input("Play another game (yes or no?): ")
        playAgain = playAgain.lower()
        if playAgain[0] != 'y' == True:
        
            return (playAgain[0] == 'y')
 
 
def main():
    game = DicePoker()
    game.playGame()
 
    
main()
