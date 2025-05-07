import json
from pathlib import Path
import sys

def main():

    uj = Path("user.json")
    if len(uj.read_text()) == 0:
        username = input("Username: ")
        password = input("Password: ")
        age = input("Age: ")

        udict = {

            "username" : username,

            "password" : password,

            "age" : age


        }

        json.dumps(udict)
    else:
        print(uj.read_text())

    """ 10-11 and 10-12: fnj = Path("favnum.json")

    if not(len(fnj.read_text()) == 0):
        favnum = fnj.read_text()
        favnum = json.loads(favnum)
        print("favorite number: " + str(favnum))
    else:
        favnum = input("give me your favorite number: ")
        favnum = json.dumps(favnum)"""
    






main()

"""10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message “I know your favorite
number! It’s _____.”
10-12. Favorite Number Remembered: Combine the two programs you wrote in
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
10-13. User Dictionary: The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.
10-14. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who last
used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username."""