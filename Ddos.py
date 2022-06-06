GNU nano 6.3          attack.py

#!/bin/python

# module
import os,sys,time

# pembersih texs
def bersih():
    os.system("clear")

# tampilan
def menu():
    bersih()
    print("\033[36;1m ")
    os.system("figlet attack")
    print("# Author : 4ndricyber")
    print("=======================================")
    print("          Daftar Menu")
    print("1). Attack Website")
    print("2). Update Script")
    print("=======================================")
menu()
