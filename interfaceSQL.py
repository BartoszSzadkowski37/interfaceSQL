
# IMPORTING MODULES
import sqlite3
import pyinputplus as pyip
import functions as func



# MAIN LOOP
loop = True

while loop:
   func.clear()
   action = func.menu() 
   if action == '1':
       func.clear()
       func.createDB()
   elif action == '2':
       func.clear()
       print('show')
   elif action == '3':
       func.clear()
       loop = False



