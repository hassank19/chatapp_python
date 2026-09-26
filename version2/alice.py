import socket
import threading


def set_connection(name, recipient): #function to connect client (current user) with server 

    client = socket.socket()
    client.connect(("127.0.0.1", 4000))

    raw = f"{name}|{recipient}" #how will server know who is sending and whom to send, we send our name and receiver's name
    client.send(raw.encode())

    def display_msg(text, sender):
        if (recipient == sender):
            print(f"\n{recipient} Replied: ", text)


    def send():
        while True:
            my_text = input("\nEnter your message: ")
            client.send(my_text.encode())
    def recvieve():
        while True:
            my_info = client.recv(2048).decode()
            sender, my_text = my_info.split("|")
            display_msg(my_text, sender)

    thread1 = threading.Thread(target=send)
    thread2 = threading.Thread(target=recvieve)
    thread1.start()
    thread2.start()



set_connection("alice", "peter")