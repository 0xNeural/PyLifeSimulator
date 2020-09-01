#Import
import os
import sys
import sqlite3
from resources.database.connect import connection, cursor
#------
validcommands = ['exit']

def themaininput():
    maincommands = input(Colors.WHITE + "\nInsert commands here: ")
    if maincommands == 'exit':
       os.system('clear')
       sys.exit()
    elif maincommands not in validcommands:
       Main.start()
       print(Colors.RED + "The command doesn't exists")
       return themaininput()

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

class Main():
    def printinfos():
        cursor.execute("SELECT * FROM session")
        infos = cursor.fetchone()
        print(Colors.BLUE + "Name: " + Colors.WHITE + infos[1] + " " + infos[2])
        print(Colors.BLUE + "Money: " + Colors.WHITE + infos[3] + "$")
        print(Colors.BLUE + "Location: " + Colors.WHITE + infos[4])
        print(Colors.BLUE + "Time: " + Colors.WHITE + infos[5] + ":" + infos[6])
        print(Colors.BLUE + "Day: " + Colors.WHITE + infos[10] + ", " + infos[7] + "/" + infos[8] + "/" + infos[9])
        print("▬▬▬▬▬▬▬▬▬▬▬")
    def start():
        os.system('clear')
        print(Colors.WHITE + "Main Menu")
        print("▬▬▬▬▬▬▬▬▬▬▬")
        Main.printinfos()