class User:
    #user_number = 0 #this is to store a unique static variable for every user, which will be the index of the user object in the users list, for first user itll be 1, for tenth itll be 10
    users = []
    def __init__(self, username, age, password):
        self.username = username
        self.age = age
        self.password = password
        User.users.append(self) #append the users list everytime we make an object


class Message:
    def __init__(self, time, isfrom, isto, text):
        self.time = time
        self.isfrom = isfrom
        self.isto = isto
        self.text = text

    def get_info(self):
        print(f"Time: {self.time}")
        print(f"Sender: {self.isfrom}")
        print(f"Receiver: {self.isto}")
        print(f"Message: {self.text}")