from asyncore import read
from engine.GameSetup import GameSetup
from engine.Utils import Utils

class Yams:
    def __init__(self):

        # clear the console and display the main presentation
        Utils.clearConsole()
        Utils.display(Yams.getPresentation())

        # init a new GameSetup
        GameSetup()

    @staticmethod
    def getPresentation():
        """
        This method opens the presentation file and returns read it
        """

        presentation = open("./src/presentation.txt", "r")
        return presentation.read()

# launch the game
Yams()