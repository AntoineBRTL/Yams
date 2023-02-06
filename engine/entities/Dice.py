from random import randint

class Dice:
    """
    Dice
    """
    def __init__(self):
        self.value = 1

    def roll(self):
        """
        This method rolls the dice, it gives a random value between 1 & 6
        """

        value = randint(1, 6)
        self.value = value

        return value

    @staticmethod
    def getValues(dices : list):
        """
        This method returns a list of the values of the given dices
        """

        dicesValue = [None] * len(dices)

        for i in range(len(dices)):
            dicesValue[i] = dices[i].value

        return dicesValue

    @staticmethod
    def isYams(dicesValue : list):
        """
        This method returns if the given dices form a "YAMS"

        -> 5 same values
        """
        return Dice.hasValuesFrequency(dicesValue, 5)

    @staticmethod
    def isBrelan(dicesValue : list):
        """
        This method returns if the given dices form a "BRELAN"

        -> 3 same values
        """

        return Dice.hasValuesFrequency(dicesValue, 3)
        
    @staticmethod
    def isSquare(dicesValue : list):
        """
        This method returns if the given dices form a "SQUARE"

        -> 4 same values
        """

        return Dice.hasValuesFrequency(dicesValue, 4)

    @staticmethod
    def isFull(dicesValue : list):
        """
        This method returns if the given dices form a "FULL"

        -> Brelan & Pair
        """

        return Dice.isBrelan(dicesValue) and Dice.isPair(dicesValue)

    @staticmethod
    def isPrime(dicesValue : list):
        """
        This method returns if the given dices form a "PRIME"

        -> Value >= 63
        """

        return sum(dicesValue) >= 63

    @staticmethod
    def isPair(dicesValue : list):
        """
        This method returns if the given dices form a "PAIR"

        -> 2 same values
        """

        return Dice.hasValuesFrequency(dicesValue, 2)

    @staticmethod
    def isBigSuite(dicesValue : list):
        """
        This method returns if the given dices form a "BIG SUITE"

        -> 1, 2, 3, 4, 5
        -> 2, 3, 4, 5, 6
        """

        if(
            (
                1 in dicesValue and 
                2 in dicesValue and
                3 in dicesValue and
                4 in dicesValue and
                5 in dicesValue
            ) 
            or 
            ( 
                2 in dicesValue and
                3 in dicesValue and
                4 in dicesValue and
                5 in dicesValue and
                6 in dicesValue
            )
        ): 
            return True

        return False

    @staticmethod
    def isSmallSuite(dicesValue : list):
        """
        This method returns if the given dices form a "SMALL SUITE"

        -> 1, 2, 3, 4
        -> 2, 3, 4, 5
        -> 3, 4, 5, 6
        """

        if(
            (
                1 in dicesValue and 
                2 in dicesValue and
                3 in dicesValue and
                4 in dicesValue 
            ) 
            or 
            ( 
                2 in dicesValue and
                3 in dicesValue and
                4 in dicesValue and
                5 in dicesValue 
            )
            or
            ( 
                3 in dicesValue and
                4 in dicesValue and
                5 in dicesValue and
                6 in dicesValue 
            )
        ): 
            return True

        return False

    @staticmethod
    def hasValuesFrequency(dicesValue : list, frequency : int):
        """
        This method checks if the dices value given contain the same dices 
        """

        numberOfSameDices = 1
        
        for i in range(len(dicesValue)):

            numberOfSameDices = 1
          
            for j in range(len(dicesValue)):
                if(i != j):
                    if(dicesValue[i] == dicesValue[j]):
                        numberOfSameDices += 1

            if(numberOfSameDices == frequency):
                return True
        return False