from classes import User
from classes import Message
from datetime import datetime

user1 = User("Alice", 20)
user2 = User("Bob", 21)

def after_login(sender):
    #for user in User.users:
        #print(f"{user.username}") #couldve done this aswell but itd be very limited
    print("Choose an operation: ")
    print("---------------")
    while True:
        operation = int(input("1: Send a message \n2: View chat history \n3: Exit\n---------------\n")) #menu based operations
        if (operation == 1):
            print("Send a message to:\n")
            #for loop to make the user choose the person they want to send the message
            for x in range(len(User.users)): #just take the length of the list so that we can enumerate it (it will make it easy to find sender and receiver based on index)
                if (sender.username == User.users[x].username):
                    print(f"{x+1}: {User.users[x].username} (You)") #if the current user is found in the list users, it will just print the option to message yourself, and then conitnue after incrementing
                    continue
                print(f"{x+1}: {User.users[x].username}")

            choice = int(input("Enter the number: "))

            receiver = User.users[choice-1] #reciever here is storing an object 

            my_text = input(f"Enter your message to {receiver.username}: ")
            timestamp = datetime.now().strftime("%I:%M:%S %p")
            message1 = Message(timestamp, sender.username, receiver.username, my_text)
            #message1.get_info()
            with open("messageinfo.txt", "a") as msginfo:
                msginfo.write(f"Time: {message1.time}, From: {message1.isfrom}, To: {message1.isto}, Text: {message1.text}\n")
            print("---------------")
        elif (operation == 2):
            with open("messageinfo.txt", "r") as msginfo:
                for line in msginfo:
                    print(f"{line}\n")
            print("---------------")
        elif (operation == 3):
            print("---------------")
            print("Exited")
            print("---------------")
            break

#-----------------------------------------------------
print("---Login---")
for x in range(len(User.users)): 
    print(f"{x+1}: {User.users[x].username}")


login_ui = int(input("Enter the number to login: "))
print("---------------")
sender_temp = User.users[login_ui - 1] #this is storing the object at that index

after_login(sender_temp)
