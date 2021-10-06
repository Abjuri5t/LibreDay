# interact with the webpage, incluce os.sytem() injection vulnerability

# input: reads from file "input.txt". Takes the Student ID from there - I.E. the file "input.txt" could contain the value '0' output: will "compile" user information and return a pretty PDF of their class schedule to the file "calendar.pdf"


import os
import time


def parseInput(fname):
    usr = ""
    with open(fname) as inFile:
        usr = inFile.readline()
    usr = usr.rstrip()
    return usr


# moves user's calendar to "./calendar.pdf" for the web app
def getCalendar(usr):  # calendars have been pre-compiled... we removed that function for simplicity  ;-)
    base = "cp users/"
    specificAndDest = "/pre-compiled-calendar.png ./pre-compiled-calendar.png"
    cmd = base + usr + specificAndDest
    os.system(cmd)
    os.system("cp ./pre-compiled-calendar.png /var/www/html/pre-compiled-calendar.png")


while(True):
    time.sleep(4)
    uname = parseInput("/input.txt")
    if(uname != "null"):
        getCalendar(uname)
