import socket
import threading

client = socket.socket()
client.connect(("127.0.0.1", 4000))

receiver = "bob"

def talk(name, recipient):

    raw = f"{name}|{recipient}" #how will server know who is sending and whom to send, we send our name and receiver's name
    client.send(raw.encode())

    def display_msg(text, sender):
        if (recipient == sender):
            print(f"\n{sender} Replied: ", text)


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


def sign_up():
    print("SINGUP")
    user = input("Enter a username: ").strip()
    passw = input("Enter your password: ").strip()
    request = f"{'SIGNUP'}|{user}|{passw}"
    client.send(request.encode())
    server_response = client.recv(2048).decode()
    if server_response == "1":
        print("Signing in...")
        talk(user, receiver)
    else:
        print("Username already exists, try another")


def login():
    print("LOGIN")
    user = input("Enter your username: ").strip()
    passw = input("Enter your password: ").strip()
    request = f"{'LOGIN'}|{user}|{passw}"
    client.send(request.encode())
    server_response = client.recv(2048).decode()
    if server_response == "1":
        print("Logged in, welcome back")
        talk(user, receiver)
    else:
        print("Incorrecr credentials")


while True:
    ui = int(input("1: Sign Up\n2: Login\n3: Exit\nChoose an operation: "))
    if ui == 1:
        sign_up()
    elif ui == 2:
        login()
    elif ui == 3:
        break


