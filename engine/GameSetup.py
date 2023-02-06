from .Utils import Utils
from .entities.Player import Player
from .entities.Dice import Dice
from .Game import Game

class GameSetup:
    """
    Setup a new game
    """
    def __init__(self):

        # generate players & dices
        self.players = GameSetup.generatePlayers()
        self.dices = GameSetup.generateDices()

        # start a new game
        Game(self.players, self.dices)

    @staticmethod
    def generatePlayers():
        """
        This method asks the user number of player in-game, their type (machine or human), their name, creates them, adds them to a list & returns it
        """
        # create an empty list which will contain all the players in-game
        numberOfPlayersPossibilities = [x for x in range(2, 10)]
        numberOfPlayers = Utils.askUser('\033[94m' + "How many players do you want in the game ?" + '\x1b[0m', numberOfPlayersPossibilities)
        playersInGame = [None] * int(numberOfPlayers)

        for i in range(len(playersInGame)):

            # to create a player, we need his:
            # type -> "human" or "machine"
            # name -> what the user wants

            # get the type
            playerTypePossibilities = ["human", "machine"]
            playerTypeMessage = '\033[94m' + "Write the " + '\033[91m' + "TYPE" + '\033[94m' + " of the player (machine or human) " + '\033[91m' + str(i + 1) + '\x1b[0m'  # NB : i + 1 is only to make the question clearer
            playerType = Utils.askUser(playerTypeMessage, playerTypePossibilities)                                                                                       

            # get the name
            playerNameMessage = '\033[94m' + "Write the " + '\033[91m' + "NAME" + '\033[94m' + " of the player " + '\033[91m' + str(i + 1) + '\x1b[0m'  # NB : same here
            playerName = Utils.askUser(playerNameMessage)                                                                                              

            # instantite a new player & add it to players in-game
            playersInGame[i] = Player(playerType, playerName)

        return playersInGame

    @staticmethod
    def generateDices():
        """
        This method generates a list of 5 dices and returns it
        """
        # create an empty list which will contain all the dices in-game
        dicesInGame = [None] * 5                                                                                # NB : there are 5 dices in the YAMS 
        
        for i in range(len(dicesInGame)):

            # instantite a new Dice and add it to the dices in-game
            dicesInGame[i] = Dice()

        return dicesInGame