# import only system from os
from os import system, name

class Utils:

    @staticmethod
    def askUser(message, possiblities = None):  
        """
        This method asks something to the user
        """

        # add a \n after the message so it's cleaner
        message = message + "\n"

        # create a variable that will contain the response 
        userRes = input(message)

        if(possiblities == None):
            return userRes

        for i in range(len(possiblities)):
            possiblities[i] = str(possiblities[i])          # NB : because the res from the user is an int, we can't compare int with str ...

        while(not userRes in possiblities):
            # show an error & re-ask
            Utils.display("ERROR")
            userRes = input(message)

        return userRes

    @staticmethod
    def clearConsole():
        """
        This method clears the console
        """

        # for windows
        if name == 'nt':
            system('cls')
    
        # for mac and linux(here, os.name is 'posix')
        else:
            system('clear')

    @staticmethod
    def display(strToDisplay):
        """
        This method display the given string to the screen
        """

        # print our message -> it's easy to change this method if we want a cleaner GUI
        print(strToDisplay)