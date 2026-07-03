from classes import User
from classes import Message
from datetime import datetime

def search_msg(sender, reciever):
    current_user = sender.username
    current_reciever = reciever.username
    search_result = []
    found = False
    string = input("Enter your query: ").strip()
    try:
        with open("messageinfo.txt", "r") as chatfile:
            for line in chatfile:
                parts = line.strip().split(", ")
                msg_sender = parts[1].replace("From: ", "")
                msg_reciever = parts[2].replace("To: ", "")
                my_text = parts[3].replace("Text: ", "")
                if ((current_user == msg_sender and current_reciever == msg_reciever) or (current_user == msg_reciever and current_reciever == msg_sender)) and string in my_text:
                    found = True
                    search_result.append(f"{line}\n")    
            if found:
                print(search_result)
            else:
                print(f"No search results for {string}")    
            
    except FileNotFoundError:
        print("Something went wrong")


def send_msg(sender, receiver):
    my_text = input(f"Enter your message to {receiver.username}: ")
    timestamp = datetime.now().strftime("%I:%M:%S %p")
    message = Message(timestamp, sender, receiver, my_text)
    #message1.get_info()
    with open("messageinfo.txt", "a") as msginfo:
        msginfo.write(f"Time: {message.time}, From: {message.isfrom.username}, To: {message.isto.username}, Text: {message.text}\n")
    print("---------------")


#in view history, we take the current users username and current receivers username
#then we open file of messages, then in a line, we split on the basis of "," so for every part seperated by a comma, it will get stored in a list (here parts) as an element at index 0-3
# so parts[0] = the time part of the message, parts[1] = the from part, parts[2] is the isto part, THATS WHAT SPLIT DOES 
def view_history(sender, receiver):
    current_user = sender.username
    current_reciever = receiver.username
    try:
        with open("messageinfo.txt", "r") as msginfo:
            for line in msginfo:
                parts = line.strip().split(", ")
                if len(parts) >= 4: #if there are at least 4 parts in list or more like time, sender, receiver, text, only then continue, if less then something is wrong
                    msg_sender = parts[1].replace("From: ", "") #remove the from from the 2nd part of list, and only keep the username string
                    msg_reciever = parts[2].replace("To: ", "") #same here
                    if (current_user == msg_sender and current_reciever == msg_reciever) or (current_user == msg_reciever and current_reciever == msg_sender): #if the username of the current sender and receiver object matches the sent from and is to names in the file then only it will print
                        print(f"{line}\n")
                        print("---------------")
                    #else:
                        #print("No messages found")
                        #print("---------------")
    except FileNotFoundError:
        print("Chat history not found")


def delete_messages(sender, reciever):
    current_sender = sender.username
    current_reciever = reciever.username
    msg_found = False
    lines_to_keep = []
    try:
        with open("messageinfo.txt", "r") as chatfile:
            for line in chatfile:
                parts = line.strip().split(", ")
                if len(parts) >= 4:
                    msg_sender = parts[1].replace("From: ", "")
                    msg_reciever = parts[2].replace("To: ", "")
                    if (current_sender == msg_sender and current_reciever == msg_reciever) or (current_sender == msg_reciever and current_reciever == msg_sender):
                        msg_found = True
                        continue
                    else:
                        lines_to_keep.append(line)
        if msg_found:
            with open("messageinfo.txt", "w") as chatfile: #i did line = line.replace(text, ""), but that didnt work, python doesnt change files like that.
                chatfile.writelines(lines_to_keep) #so the better way is to store the messages you dont want to delete, then overrite the file with those messages, thus 'w'
                print("Messages deleted")
                print("---------------")
        else:
            print("No messages found")
            print("---------------")
    except FileNotFoundError:
        print("Something went wrong")

def after_login(sender):
    #for user in User.users:
        #print(f"{user.username}") #couldve done this aswell but itd be very limited
    print("Choose an operation: ")
    print("---------------")
    while True:
        operation = int(input("1: Send a message \n2: View chat history \n3: Delete messages \n4: Search messages \n5: Exit \n---------------\n")) #menu based operations
        if (operation == 1):
            print("Send a message to:\n")
            #for loop to make the user choose the person they want to send the message
            for x in range(len(User.users)): #just take the length of the list so that we can enumerate it (it will make it easy to find sender and receiver based on index)
                if (sender.username == User.users[x].username):
                    print(f"{x+1}: {User.users[x].username} (You)") #if the current user is found in the list users, it will just print the option to message yourself, and then conitnue after incrementing
                    continue
                print(f"{x+1}: {User.users[x].username}")
            choice = int(input("Enter the number: "))
            reciever = User.users[choice-1] #reciever here is storing an object 
            send_msg(sender, reciever)

        elif (operation == 2):
            print("View your chat history with: ")
            for x in range(len(User.users)): #just take the length of the list so that we can enumerate it (it will make it easy to find sender and receiver based on index)
                if (sender.username == User.users[x].username):
                    print(f"{x+1}: {User.users[x].username} (You)") #if the current user is found in the list users, it will just print the option to message yourself, and then conitnue after incrementing
                    continue
                print(f"{x+1}: {User.users[x].username}")
            choice = int(input("Enter the number: "))
            reciever = User.users[choice-1] #reciever here is storing an object 
            view_history(sender, reciever)

        elif (operation == 3):
            print("Delete a message in your chat with: ")
            for x in range(len(User.users)):
                if (sender.username == User.users[x].username):
                    print(f"{x+1}: {User.users[x].username} (You)") #if the current user is found in the list users, it will just print the option to message yourself, and then conitnue after incrementing
                    continue
                print(f"{x+1}: {User.users[x].username}")
            choice = int(input("Enter the number: "))
            reciever = User.users[choice-1]
            delete_messages(sender, reciever)

        elif (operation == 4):
            print("Search messages with: ")
            for x in range(len(User.users)):
                if (sender.username == User.users[x].username):
                    continue
                print(f"{x+1}: {User.users[x].username}")
            choice = int(input("Enter the number: "))
            reciever = User.users[choice-1]
            search_msg(sender, reciever)


        elif (operation == 5):
            print("---------------")
            print("Exited")
            print("---------------")
            break

#-----------------------------------------------------
def find_user_index_inlist(uid):
    index = 0
    for x in range(len(User.users)):
        if uid == User.users[x].username:
            index = x
            break
    return index



def login():
    user_id = input("Enter your username: ")
    password = input("Enter a password: ")
    found = False
    with open("udatabase.txt", "r") as database:
        for line in database:
            parts = line.strip().split(", ")
            username_ = parts[0].strip()
            pass_ = parts[2].strip()
            if (user_id == username_) and (password == pass_):
                found = True
                break
    if found:
        print("Logged In!")
        index = find_user_index_inlist(user_id)
        current_user = User.users[index]
        after_login(current_user)
    else:
        print("Invalid user or password, try again?")


def sign_up():

    user_id = input("Enter a username: ")
    password = input("Make a password: ")
    found = False
    with open("udatabase.txt", "r") as database:
        for line in database:
            parts = line.strip().split(", ")
            username_ = parts[0].strip()
            pass_ = parts[2].strip()
            if (user_id == username_):
                found = True
                break
    if found:
        print("Username already exists, try another username")
    else:
        age = int(input("Enter your age: "))
        new_user = User(user_id, age, password)
        with open("udatabase.txt", "a") as database:
            database.write(f"{new_user.username}, {new_user.age}, {new_user.password}\n")
        print("Signed in")
        index = find_user_index_inlist(user_id)
        current_user = User.users[index]
        after_login(current_user)


def load_users(): #whenever u run the code, the new users created after signing in are stored permennantly in the database file, but theyre stored in the User.users lists only until the runtime, so once program ends, the list becomes empty
    with open("udatabase.txt", "r") as database: #by loading (reading database file) and appending in the list, we make all the operations possible
        for line in database: #otherwise we would just have an empty list
            parts = line.strip().split(", ")
            user = parts[0]
            age = parts[1]
            passw = parts[2]
            new_user = User(user, age, passw)


load_users()
ui = int(input("1: Sign Up\n2: Login \nChoose an operation: "))
if ui == 1:
    sign_up()
if ui == 2:
    login()

#login_ui = int(input("Enter the number to login: "))
#print("---------------")
#sender_temp = User.users[login_ui - 1] #this is storing the object at that index

#after_login(sender_temp)