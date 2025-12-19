# Functions within a larger function:

from datetime import datetime

def Greetings():
    name = input("Enter your name: ")
    print("Welcome, {}!".format(name))
    return name
def getTime():
    currentTime = datetime.now()
    time_string = currentTime.strftime("%H:%M:%S")
    print("Current time {}".format(time_string))
def getUserNameAndEmail():
    mail = input("Enter your email: ")
    return mail
def printDetails():
    name = Greetings()
    mail = getUserNameAndEmail()
    print("\nUser details: ")
    print("Name: {}\nEmail: {}".format(name,mail))
    getTime()

printDetails()
