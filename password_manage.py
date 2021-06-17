# This is a Password Manager Script.
# It takes input from the user and create a .txt file and save it to the directory.

import os

title = input("Enter the name of the platform :- ")
email = input("What Email-Id did you use their :- ")
username = input("What Username did you use their :- ")
password = input("What was the password :- ")


if __name__ == "__main__":

    os.chdir("D:/pass_man")                     # Change the directory where you want to locate the Password file

    file = open(title + ".txt", "a", encoding='utf-8')
    file.write("platform :- " + title + "\n")
    file.write("Email-Address :- " + email + "\n")
    file.write("user name :- " + username + "\n")
    file.write("password :- " + password + "\n")
    file.write("\n")
