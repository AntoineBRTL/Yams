from .Dice import Dice
from ..Utils import Utils
from ..Game import Game

class Player:
    def __init__(self, type, name):
        self.type = type
        self.name = name

        self.log = '\033[91m' + name.upper() + '\033[94m' + " (" + type + ")" + '\x1b[0m'

        self.points = 0     # 0 by default

    def play(self, dices : list):
        """
        This method make the player play
        """

        # type == machine -> only roll his dices
        if(self.type == "machine"):
            return self.rollDices(dices)

        # type == "human"
        rollPossibilities = ["yes", "no"]
        rollMessage = '\033[94m' + "Do you wanna roll your dices ?" + '\x1b[0m'

        if(Utils.askUser(rollMessage, rollPossibilities) == "yes"):
            self.rollDices(dices)
        else:
            return None     # -> the player don't play

        # possibility to roll 2 more times the dices you want
        for roll in range(2):

            # display the possible new points
            dicesValue = Dice.getValues(dices)
            possibleNewPoints = Game.countPoints(dices, self.log)
            Utils.display('\033[91m' + "POSSIBILITY" + '\033[94m' + " : +" + str(possibleNewPoints) + " ----> " + str(self.points + possibleNewPoints) + '\x1b[0m' + " : " + ", ".join([str(x) for x in dicesValue]))

            reRollMessage = '\033[94m' + "Re-roll your dices ? " + '\x1b[0m' + "(" + '\033[91m' + str(roll + 1) + '\x1b[0m' + "/2" + ")"
            if(Utils.askUser(reRollMessage, rollPossibilities) == "yes"):

                # loop over each dices to ask if the player want to re-roll it
                chosenDices = []

                for i in range(len(dices)):
                    specificDiceMessage = '\033[94m' + "Dice " + '\033[91m' + str(i + 1) + '\033[94m' + " -> " + '\033[91m' + str(dicesValue[i]) + '\x1b[0m'
                    if(Utils.askUser(specificDiceMessage, rollPossibilities) == "yes"):
                        chosenDices.append(dices[i])

                self.rollDices(chosenDices)

            else:
                return dices

        return dices

    def rollDices(self, dices : list):
        """
        This method roll the given dices & display their values
        """

        for dice in dices:
            dice.roll()

        dicesValue = Dice.getValues(dices)
        Utils.display(", ".join([str(x) for x in dicesValue]))

        return dices