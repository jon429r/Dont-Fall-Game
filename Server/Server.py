##DONE
##Server.py

import socket
import argparse
import threading

import User
from Map import map_command
from GameCommands import hello_command, quit_command, movement_command, leaderboard_command, chatbox_command, info_command
from OtherCommands import parse_input
from GameTimer import start_game_timer, game_info, map_update_timer


def client_handle(client, address):
    """Handles the client connection and commands
    
    Args:
    client (client): Is the client socket used to send messages
    address (address): Is the address of the client socket
    """

    print('Connected to client at', address)
    ## Main loop to handle the client
    ## The loop will only stop when the connection is broken
    ## The loop will receive data from the client, decode it, 
    ##find what command type it is, and call the correct command 
    ##function depending on the command entered
    while True:
        try:
            data = client.recv(1024)
            if not data:
                print('Client disconnected')
                return

            data = parse_input(data.decode('utf-8'))
            print('Client sent:', data)

            request_type = data[0].lower()

            if request_type == 'hello':
                try:
                    username = data[1]
                    go = hello_command(username, client)
                    if go == '200':
                        break
                except IndexError:
                    print('No username entered')
                    message = ('400 Error: Please Input A Valid Username after the Hello Command').encode('utf-8')
                    client.sendall(message)
                    continue

            if request_type == 'quit':
                quit_command(client)
                break

            else:
                message = ("""400 Error: Please Input A Valid Command\n
                           Valid Command List:
                           Hello <Username>
                           quit""").encode('utf-8')
                client.sendall(message)
        except OSError:
            print('Client disconnected')
            break


    while True:
        try:
            try:
                data = client.recv(1024)
                if not data:
                    print('Client disconnected')
                    break

                data = parse_input(data.decode('utf-8'))
                print('Client sent:', data)

                try:
                    request_type = data[0].lower()
                except TypeError:
                    print('No command entered')
                    message = ("""400 Error: Please Input A Valid Command\n
                           Valid Command List:
                           Hello <Username>
                           quit\n""").encode('utf-8')                
                    client.sendall(message)
                    continue

                # Sees what type of command is entered and routes the data to the correct function


                fallen = User.get_Fallen(client)

                print(request_type)

                if request_type == 'quit':
                    quit_command(client)
                elif request_type in ['north', 'south', 'west', 'east', 'up', 'down', 'left', 'right', 'w', 'a', 's', 'd'] and fallen is not True:
                    movement_command(request_type, client)
                elif request_type == 'map' and fallen is not True:
                    map_command()
                elif request_type == 'info':
                    info_command(client)
                elif request_type == 'leaderboard':
                    leaderboard_command(client)
                elif request_type == 'chat':
                    try:
                        message = ' '.join(data[1:])
                        chatbox_command(message, client)
                    except socket.error as e:
                        print(f"Error while sending message: {e}")

            except TypeError:
                print('Please Input A valid Command')
                message = ("""400 Error: Please Input A Valid Command\n
                       Valid Command List: \n
                        quit\n
                        movement(specify direction)\n
                        map\n
                        info\n
                        leaderboard\n
                        chat<message>\n""").encode('utf-8')
                client.sendall(message)

        except OSError as e:
            # Handle disconnection, log the error, and break out of the loop
            print(f'Error handling client data: {e}')
            # Find and remove the disconnected user from UserList
            from User import get_user, UserList
            disconnected_user = get_user(client)
            if disconnected_user:
                UserList.remove(disconnected_user)
            break
        
def main():
    """Main function that starts the server and handles the arguments
        Starts the server and listens for connections
    """

    ##Sets up arguments for the server
    ##Port is the port the server will listen on
    ##MapSize is the size of the map the server will create
    arg = argparse.ArgumentParser()

    arg.add_argument('-p', '--port', type=int, default=2042,
                     help='Port to bind the server to.')
    arg.add_argument('-m', '--mapSize', type=str, default='10x10',
                     help='Map size SizeXSize EX: 10x20')

    args = arg.parse_args()

    if args.port < 1024 or args.port > 65535:
        print('Invalid port number. Must be between 1024 and 65535.')
        exit()

    mapSize = args.mapSize.split('x')
    if len(mapSize) != 2:
        print('Invalid map size. Must be in the format of SizeXSize EX: 10x10')
        exit()

    HOST = '127.0.0.1'
    PORT = args.port
    if PORT is None:
        PORT = 8080


    ##Starts the Server
    print("Server listening on", HOST, ":", PORT)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)

    ##Starts the game timer thread
    ##An indiviual thread to handle the game timer
    start_game_timer()
    # Start the map update timer in a separate thread
    map_update_thread = threading.Thread(target=map_update_timer)
    map_update_thread.daemon = True  # Allow the program to exit even if this thread is still running
    map_update_thread.start()

    ##Main loop to listen for connections
    while True:
        c, addr = s.accept()
        print('Accepted connection from', addr)

        try:
            game_info()
            client_thread = threading.Thread(target=client_handle, args=(c, addr))
            client_thread.start()
        except TypeError as e:
            print('Error in client_handle:', str(e))

    s.close()

if __name__ == "__main__":
    main()