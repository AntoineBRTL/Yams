from .entities.Dice import Dice
from .Utils import Utils

class Game:
    """
    The Yams game : 

    -> play 10 rounds
    -> counts points
    -> display the winner
    """
    def __init__(self, players : list, dices : list):

        # get the players and the dices for the current game
        self.players = players
        self.dices = dices

        # init the 10 rounds
        for i in range(10):
            self.playRound(i)

        # display the winner
        winner = Game.getWinner(players)
        winnerMessage = '\033[94m' + "Congratulation to you " + '\033[91m' + winner.name.upper() + '\033[94m' + ", you won with " + '\033[91m' + str(winner.points) + '\033[94m' + " points !" + '\x1b[0m'
        Utils.display(winnerMessage)

    def playRound(self, roundIndex : int):
        """
        This method plays a round
        """

        # display a little presentation
        Utils.display("\nRound number " + str(roundIndex + 1) + "/10")
        Utils.display("-----------------")

        # make each players play the round
        for player in self.players:

            # display which player is playing
            playingPlayerMessage = player.log + '\033[94m' + " is playing ..." + '\x1b[0m'
            Utils.display(playingPlayerMessage)

            # count the score of the player and display it
            newPlayerPoints = Game.countPoints(player.play(self.dices), player.log)
            player.points += newPlayerPoints
            playerPointsMessage = player.log + '\033[94m' + " : " + '\033[91m' + "+" + str(newPlayerPoints) + '\033[94m' + " ----> " + str(player.points) + '\x1b[0m' + "\n"
            Utils.display(playerPointsMessage)

    @staticmethod
    def getWinner(players : list):
        """
        This method returns the player who have the highest score
        """

        highestScorePlayer = players[0]
      
        for i in range(1, len(players)):
            if players[i].points > highestScorePlayer.points:
                highestScorePlayer = players[i]
        
        return highestScorePlayer
      
    @staticmethod
    def countPoints(dices: list, playerLog: str):
        """
        This method counts the points of the given dices
        """

        # No dices = 0 points !!!
        if (dices == None):
            return 0

        dicesValue = Dice.getValues(dices)

        # prime
        if (Dice.isPrime(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "prime".upper())  

        # big suite
        elif (Dice.isBigSuite(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "big suite".upper()) 
            return 40

        # small suite
        elif (Dice.isSmallSuite(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "small suite".upper())  
            return 20

        # yams
        elif (Dice.isYams(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "yams".upper())  
            return 50

        # full
        elif (Dice.isFull(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "full".upper())  
            return 25

        # square
        elif (Dice.isSquare(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "square".upper())  
            return sum(dicesValue)

        # brelan
        elif (Dice.isBrelan(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "brelan".upper())  
            return sum(dicesValue)

        # pair
        elif (Dice.isPair(dicesValue)):
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "pair".upper())  
            return sum(dicesValue)

        else:
            Utils.display(playerLog + '\033[94m' + " made a " + '\033[91m' + "nothing ...".upper())  
            return sum(dicesValue)
