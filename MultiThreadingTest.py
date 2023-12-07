##AI generated test script for multithreading

import socket
import threading
import time
import random

def send_message(sock, message):
    sock.sendall(message.encode('utf-8'))

def receive_message(sock):
    data = sock.recv(1024)
    return data.decode('utf-8')

def user_simulation(username):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 2042))

        # Simulate the 'hello' command
        send_message(s, f'hello {username}')
        response = receive_message(s)
        print(response)

        # Simulate various game commands
        commands = ['north', 'south', 'west', 'east', 'up', 'down', 'left', 'right', 'w', 'a', 's', 'd', 'map', 'info', 'leaderboard']
        for _ in range(5):  # Simulate 5 random commands
            command = random.choice(commands)
            send_message(s, command)
            response = receive_message(s)
            print(response)

            time.sleep(1)  # Wait for a while between commands

        # Simulate the 'chat' command
        chat_message = f'hello from {username}'
        send_message(s, f'chat {chat_message}')
        response = receive_message(s)
        print(response)

        # Simulate the 'quit' command
        send_message(s, 'quit')
        response = receive_message(s)
        print(response)

# Simulate multiple users
usernames = ['User1', 'User2', 'User3', 'User4', 'User5', 'User6', 'User7', 'User8', 'User9', 'User10']

threads = []
for username in usernames:
    thread = threading.Thread(target=user_simulation, args=(username,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
