#AI generated test script for signle threading

import socket
import time

def send_command(sock, command):
    sock.sendall(command.encode('utf-8'))
    response = sock.recv(1024).decode('utf-8')
    print(response)

def main():
    # Replace '127.0.0.1' and 2042 with your server's IP address and port
    server_address = ('127.0.0.1', 2042)

    try:
        # Create a socket connection to the server
        with socket.create_connection(server_address) as sock:
            print("Connected to the server.")

            # Testing the hello_command
            send_command(sock, 'hello Carter')

            # Introduce some delay to allow the server to process the hello command
            time.sleep(1)

            # Testing movement_command
            send_command(sock, 'north')

            # Introduce some delay to allow the server to process the movement command
            time.sleep(1)

            # Testing leaderboard_command
            send_command(sock, 'leaderboard')

            # Introduce some delay to allow the server to process the leaderboard command
            time.sleep(1)

            # Testing chatbox_command
            send_command(sock, 'chat hello world')

            #Testing quit_command
            send_command(sock, 'quit')

    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
