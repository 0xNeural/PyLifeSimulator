#Import
import os
import sqlite3
from resources.database.connect import connection, cursor
from game import Main as GameMain 
from game import themaininput
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
    def UpdateSession(NAME, SURNAME, MONEY, LOCATION):
        connection.execute("UPDATE session SET name=?", [NAME])
        connection.execute("UPDATE session SET surname=?", [SURNAME])
        connection.execute("UPDATE session SET money=?", [MONEY])
        connection.execute("UPDATE session SET location=?", [LOCATION])
        connection.commit()
        
    def menu():
        print(Colors.YELLOW + "New Game\n")
        namepg = input(Colors.GREEN + "Inserisci il nome del tuo personaggio: ")
        surnamepg = input(Colors.GREEN + "Inserisci il cognome del tuo personaggio: ")
        print("")
        ready = input(Colors.GREEN + "Are you ready? (Y/n): ")
        sessioname = namepg + surnamepg
        Main.UpdateSession(namepg, surnamepg, '1000', "Parent's house")
        GameMain.start()
        themaininput()







