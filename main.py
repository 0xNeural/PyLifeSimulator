#Import
import os
from newgame import Main as NewGame
#------
class Colors():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class Main:
    def title():
        os.system('clear')
        print(Colors.RED + "PyLifeSimulator v0.1")
        print(Colors.RED + "Created by Neural0x\n")
    def menu():
        print(Colors.YELLOW + "Main Menu\n")
        print(Colors.YELLOW + "1. New Game")
        print(Colors.YELLOW + "2. Load Game")
        print(Colors.YELLOW + "3. Settings\n")
        mainscelta = input(Colors.GREEN + "Inserisci un opzione: ")
        if(mainscelta == "1"):
           Main.title()
           NewGame.menu()
 
Main.title()
Main.menu()