# THIS PROGRAM EXISTS FOR PRACTICE SQL QUERIES

import sqlite3
import pyinputplus as pyip


con = sqlite3.connect('practice.db')

con.row_factory = sqlite3.Row

cur = con.cursor()

mainLoop = True

while mainLoop:

    query = pyip
