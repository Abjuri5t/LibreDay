import sqlite3
import socket
import sys


def sendStr(connection, string):
    sendBts = str.encode(string)
    print("Sending: \""+string+'\"')
    connection.send(sendBts)


#open database
curs = sqlite3.connect("Students.db")
print("Opened DB")

#listen for connection
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(("127.0.0.1", int(sys.argv[1])))
print("Socket binding operation complete")
serv.listen(5)
conn, addr = serv.accept()
print("Connected with "+addr[0]+':'+str(addr[1]))

#first prompt
sendStr(conn, "Enter potential studentId number (single digit): ")
sId1 = conn.recv(1024).decode()
xtraQueries = []
firstQuery = "SELECT isStudent FROM Students WHERE studentId="+sId1
if(';' in firstQuery):
    xtraQueries = firstQuery.split(';')
    firstQuery = xtraQueries.pop(0)
print("Running: \""+firstQuery+'\"')
result = curs.execute(firstQuery)
for xQry in xtraQueries:
    print("Running: \""+xQry+'\"')
    curs.execute(xQry)
for row in result:
    art = str(row).split('\'')[1]
    if("yes" in art):
        sendStr(conn, "Given ID is a student.")
    else:
        sendStr(conn, "ID is not a known student (may be teacher?)")

#second prompt
sendStr(conn, "Enter studentId number to check grades: ")
sId2 = conn.recv(1024).decode()
if(('\"' in sId2) or ('\'' in sId2) or (';' in sId2)):
    sendStr(conn, "Ahh!!!! injection detected in input for second query!")
elif(("1" not in sId2) and ("2" not in sId2)):
    sendStr(conn, "Given ID does not match any known student.")
else:
    secondQuery = "SELECT grade FROM Students WHERE studentId="+sId2
    print("Running: \""+secondQuery+'\"')
    result = curs.execute(secondQuery)
    for row in result:
        art = str(row).split('\'')[1]
        if(("QQ==" in art) or ("Qg==" in art) or ("Qw==" in art)):
            sendStr(conn, "Student is passing Network Security.\nCelebratory message will be displayed here...  ;-)")
        else:
            sendStr(conn, "Student is not passing class.")


conn.close()
