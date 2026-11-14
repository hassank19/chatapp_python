# Python Client-Server Chat Application

A basic real-time messaging application built using Python, TCP sockets, multithreading and SQLite.

The purpose of this project was to understand how client-server communication works, how multiple clients interact with a central server, and how messages can be exchanged and stored using Python.

This is a learning project and is not intended to be a production-ready messaging application.

## Features

- **User Registration:** Users can create accounts with a username and password.
- **User Authentication:** Existing users can log in using their credentials.
- **TCP Socket Communication:** Clients communicate with a central server using Python's `socket` module.
- **Multithreading:** Separate threads handle sending and receiving messages, allowing simultaneous communication.
- **Real-Time Messaging:** Messages are forwarded to recipients who are currently connected to the server.
- **Online User Tracking:** A Python dictionary keeps track of connected users and their respective socket connections.
- **Message Persistence:** Messages are stored in an SQLite database, regardless of whether the recipient is online or offline.

## Technologies Used

| Technology | Purpose                                 |
| ---------- | --------------------------------------- |
| Python     | Core programming language               |
| Socket     | TCP client-server communication         |
| Threading  | Concurrent sending and receiving        |
| SQLite3    | User authentication and message storage |
| SQL        | Database queries and operations         |

## How It Works

The application follows a client-server architecture.

1. The server listens for incoming client connections.
2. Each incoming connection is handled using a separate thread.
3. Clients can register or authenticate themselves using credentials stored in an SQLite database.
4. Once authenticated, a client specifies the intended recipient.
5. The server maintains a dictionary of currently connected users.
6. When a message is sent, the server stores it in the database.
7. If the recipient is online, the server forwards the message through their socket connection.
8. If the recipient is offline, the message remains stored in the database.

## Project Structure

```text
chatapp/
│
├── server.py
├── alice.py
├── bob.py
├── peter.py
├── userdb.db
└── mydb.db
```

To simulate 2 users communicating, run any two files among peter.py, alice.py and bob.py

## Running the Application

**Prerequisites:**

- Python 3.x
- SQLite3 (included with Python through `sqlite3`)

**Steps:**

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

2. Navigate to the project directory:

```bash
cd chatapp
```

3. Start the server:

```bash
python server.py
```

4. Open another terminal and start a client:

```bash
python alice.py
```

5. Open additional client instances to simulate multiple users.

**Note:** The current implementation binds the server to `127.0.0.1`, so clients must run on the same machine unless the networking configuration is changed.

The SQLite databases and their required tables must also be initialized before running the application.

## Known Limitations

This project is still a work in progress in terms of reliability and robustness.

Some known limitations include:

- TCP message framing has not been properly implemented. The application currently assumes that individual `send()` and `recv()` calls correspond to complete messages, which TCP does not guarantee.
- Error handling is limited, and certain unexpected inputs or connection failures can crash the application.
- Thread synchronization and concurrent access to shared resources, particularly the connected users dictionary, need improvement.
- Authentication and message handling need stronger security measures. Passwords are not currently protected using password hashing.
- Offline messages are stored in the database, but a complete mechanism for retrieving and delivering pending messages has not yet been implemented.
- The application has not been extensively tested against multiple simultaneous clients or unexpected disconnections.

## What I Learned

Building this project gave me practical experience with:

- TCP communication and socket programming.
- Client-server architecture.
- Multithreading and concurrent execution.
- Database integration using SQLite.
- SQL queries and user authentication.
- Managing connected clients using dictionaries.
- Debugging communication and concurrency-related problems.

It also helped me understand that network programming involves more than simply establishing a connection and exchanging data. Handling unexpected behaviour, synchronization and communication reliability introduces challenges of its own.

## Future Improvements

Some areas that could be explored in future iterations:

- Implementing proper TCP message framing.
- Improving error handling and connection management.
- Implementing secure password hashing.
- Synchronizing access to shared resources.
- Implementing offline message retrieval and delivery.
- Adding message delivery acknowledgements.
- Supporting communication between devices over a network.
- Developing a graphical user interface.

## Disclaimer

This project was developed as a personal learning exercise to explore Python networking and database concepts. It is not production-ready, and several edge cases and reliability issues remain unresolved.

The intention is to document what I have built, what I have learned, and what can be improved in future iterations.

**Author:** Hassan
