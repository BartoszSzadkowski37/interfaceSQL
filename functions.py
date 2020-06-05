# FUNCTIONS FOR THE SQL DB MANAGEMENT STUDIO

# IMPORTING MODULES
from os import system, name
import pyinputplus as pyip

# FUNCTION FOR CLEARING THE SCREEN
def clear():
    #for windows
    if name == 'nt':
        _ = system('cls')
    #for mac and linux
    else:
        _ = system('clear')


# FUNCTION TO PRINT MAIN MENU 
def menu():
    print('1. CREATE DATABASE')
    print('2. SHOW DATABASES')
    print('3. EXIT')
    userInput = pyip.inputChoice(['1', '2', '3'], '(1/2/3):')
    return userInput

