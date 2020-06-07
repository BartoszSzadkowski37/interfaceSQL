# SQL DB MANAGEMENT STUDIO

# 1 Menu

# WELCOME IN SQL DB MANAGEMENT STUDIO
# 1. CREATE DATABASE
# 2. SHOW DATABASES
# 3. EXIT

# CREATE DATABSE
# 1. CREATE FROM DB STUDIO LEVEL
# 2. INPUT SQL MANUALLY

# SHOW DATABASES
# show list of DBs
# IDEA FOR CHECK EXIST DBS
Python 3.7.3 (default, Dec 13 2019, 19:58:14) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> from pathlib import Path
>>> Path.cwd()
PosixPath('/Users/bartoszszadkowski/Desktop/PajtonProjects/interfaceSQL')
>>> currentPath = Path.cwd()
>>> currentPath
PosixPath('/Users/bartoszszadkowski/Desktop/PajtonProjects/interfaceSQL')
>>> os.listdir(currentPath)
['functions.py', 'interfaceSQL.py', '.DataBase.py.swp', '.ideas.py.swo', '__pycache__', '.functions.py.swp', 'ideas.py', '.interfaceSQL.py.swp', '.git', '.ideas.py.swp']
>>> import re
>>> dataBaseCheckReg = re.compile(r'.*\.db')
>>> dataBaseCheckReg.findall(os.listdir(currentPath))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: expected string or bytes-like object
>>> dbs = str(os.listdir(currentPath))
>>> dbs
"['functions.py', 'interfaceSQL.py', '.DataBase.py.swp', '.ideas.py.swo', '__pycache__', '.functions.py.swp', 'ideas.py', '.interfaceSQL.py.swp', '.git', '.ideas.py.swp']"
>>> dataBaseCheckReg.findall(dbs)
[]
>>> dataBaseCheckReg.findall(dbs)
[]
>>> os.listdir(currentPath)
['functions.py', 'interfaceSQL.py', '.DataBase.py.swp', '.ideas.py.swo', '__pycache__', 'baza.db.db', '.functions.py.swp', 'ideas.py', '.interfaceSQL.py.swp', '.git', '.ideas.py.swp']
>>> dbs = str(os.listdir(currentPath))
>>> dataBaseCheckReg.findall(dbs)
["['functions.py', 'interfaceSQL.py', '.DataBase.py.swp', '.ideas.py.swo', '__pycache__', 'baza.db.db"]


# Provide name of DB to manage or pass 'q' to exit


# DATABASE (NAME) MANAGEMENT
# to be continued ...§# show list of DBs

# Provide name of DB to manage or pass 'q' to exit


# DATABASE (NAME) MANAGEMENT
# to be continued ...§# show list of DBs

# Provide name of DB to manage or pass 'q' to exit


# DATABASE (NAME) MANAGEMENT
# to be continued ...§





