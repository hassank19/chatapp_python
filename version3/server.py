# this file will be only hosted/exist on one person's file
import socket
import threading
from datetime import datetime
import sqlite3

connected_users = {} #this dict is to see who is currently connected to server, if both sender and receiver are connected then we send in real time, if not then we will have to send the pending messages seperately

my_server = socket.socket()
my_server.bind(("127.0.0.1", 4000))

my_server.listen()


def handle(sender_sock):

    def login(u, p):
        #while True:
            found = False
            connection = sqlite3.connect("userdb.db")
            cursor = connection.cursor()
            cursor.execute("""select username from users where username = ? AND password = ?""", (u, p))
            user = cursor.fetchone() #fetches that row
            if user: #if it fetched some value, we know that credentials were correct
                server_response = "1"
                sender_sock.send(server_response.encode())
                #break
            else:
                server_response = "0" #0 and 1 are being used as succes/failed identifiers, so we can send them to the client to tell them what happened 
                sender_sock.send(server_response.encode())
            connection.commit()
            connection.close()
            

    def signup(u, p):
        #while True:
            connection = sqlite3.connect("userdb.db")
            cursor = connection.cursor()
            cursor.execute("""Select username from users where username = ?""", (u,))
            existing_user = cursor.fetchone()

            if existing_user:
                server_response = "0"
                sender_sock.send(server_response.encode())
                #break
            else:
                cursor.execute("""insert into users (username, password) values (?, ?)""", (u, p))
                server_response = "1"
                sender_sock.send(server_response.encode())
            connection.commit()
            connection.close()

    session = sender_sock.recv(2048).decode() #1st thing we receive from client is session, username and pass, ie: login/signup
    #----> the request variable in the client code
    request, sender_username, password = session.split("|")

    if request == "LOGIN":
         login(sender_username, password)
    if request == "SIGNUP":
         signup(sender_username, password)


    while True:
        raw = sender_sock.recv(2048).decode() #2nd thing we received: joint sender and receiver's name, so we split it

        username, recipient = raw.split("|")

        connection = sqlite3.connect("userdb.db") #this code is to check if the recipient username exists in our database, if it does, then we operate normally
        cursor = connection.cursor()
        cursor.execute("""select username from users where (username) = ?""", (recipient,))
        data = cursor.fetchone()
        connection.commit()
        connection.close()

        if data:
            sender_sock.send("0".encode())
            break
        else:
            sender_sock.send("1".encode())

    connected_users[username] = sender_sock #add the key-value pair to the dictionary


    while True:
            text = sender_sock.recv(2048) #receive from bob/client 1
            if not text: #if the client(bob) disconnects
                break
            decrpt_text = text.decode()
        
            connection = sqlite3.connect("mydb.db")
            cursor = connection.cursor()
            cursor.execute("""INSERT INTO messages (sender, receiver, message) values (?, ?, ?)""", (username, recipient, decrpt_text)) #store all messages in db, no matter if recipient is active or not
            connection.commit()
            connection.close()

            if recipient in connected_users: #if the recipient is also connected, then send the message

                info = f"{username}|{decrpt_text}"

                connected_users[recipient].send(info.encode()) #send to alice, along with the sender's name, so alice knows who the message is coming from, 
                #connected_users[recipient], will give us the recipient socket from the dictionary (key-value) 
            
    #when the while loop breaks (when bob or client1 disconnects), the below code will be executed    
    connected_users.pop(username, None)  #or del connected_users[username]
    sender_sock.close() #close the socket

while True: #this loop is needed to connect as many clients as we want.

    my_client, add = my_server.accept()
    my_thread = threading.Thread(target=handle, args=(my_client,))


    my_thread.start()












"""
while loop is extremely important in these programs
we use while loop to solve a lot of problems, like 1) to endlessly receive as many connections to the server,
like here 
while True: my_client, add = my_server.accept()
my_thread = threading.Thread(target=handle, args=(my_client,))
my_thread.start(),
and then to repeatedly check if the recipient client is in the dictionary, 
 while True:
        if recipient in connected_users:
    ---> because when alex connects, he is stored in dict, but the recipient bob hasnt been connected yet, so if we dont repeatedly check the dict, we will face a problem
    while loop solves this by repeatedly checking the dict to see if the recipient is now in the dict, when it is there, only then it executes the rest of the block
"""