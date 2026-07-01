class User:

    users = []

    def __init__(self, username, age):
        self.username = username
        self.age = age
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