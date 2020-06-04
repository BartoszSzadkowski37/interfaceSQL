# THIS PROGRAM EXISTS FOR PRACTICE SQL QUERIES

# Use regex to find out if query is select, if is print output

import sqlite3
import pyinputplus as pyip


con = sqlite3.connect('practice.db')

con.row_factory = sqlite3.Row

cur = con.cursor()

mainLoop = True

while mainLoop:


