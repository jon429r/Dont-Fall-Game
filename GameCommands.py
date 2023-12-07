##DONE
##GameCommands.py

from User import User, calculate_Score
from User import UserList
from User import get_user, getUsername
from OtherCommands import username_command
from Physics import collision
from GameTimer import game_info


def hello_command(username, client):
    """Creates a new user and adds them to the UserList

    Args:
        username (String): Will be the username for the new user
        client (client): Is the client socket used to send messages

    Returns:
        String: Returns a success code '200' if the user was created successfully
        Returns '400' an error code if the user was not created successfully
    """
    try:
        if username_command(username):
            # Create a new user, add them to the UserList, initialize their score and start time
            start_time = game_info()
            player = User(username, client, 3, 3, start_time, 0, calculate_Score, False)
            UserList.append(player)

            # Send a message to the client and returns a success code to the server
            message = ('200 HELLO Ok, Hello there ' + username + '\n').encode('utf-8')
            client.sendall(message)
            return '200'

        # Send an error message if the username is not valid or in use
        message = ('400 HELLO Sorry, ' + username + ' is not valid or is in use \n').encode('utf-8')
        client.sendall(message)
        return '400'
    except TypeError as e:
        print(f"Error in hello_command: {e}")
        return '400'


def quit_command(client):
    """Removes the user from the UserList and closes the client socket

    Args:
        client (client): Is the client socket used to send messages
    """
    # Gets the user from the user list and removes them from the game
    user = get_user(client)
    if user:
        print('User disconnected:', user.Username)

    message = '200 QUIT Ok, Goodbye\n'.encode('utf-8')
    client.sendall(message)

    if username_command(user) is False:
        UserList.remove(user)
    else:
        client.close()


def movement_command(direction, client) -> str:
    """Moves the user in the specified direction
        Checks to see if the user fell or collided with a wall
        if the user fell, the user is removed from the UserList

    Args:
        direction (string): The direction the user wants to move
        client (client): Is the client socket used to send messages

    Raises:
        ValueError: If the user enters an invalid direction

    Returns:
        str: Returns a success code '200' if the user was moved successfully
        Returns '400' an error code if the user was not moved successfully
    """

    # Gets the user from the user list, initializes the messages
    user = get_user(client)
    collision_message = ('400 Error: Collision \n').encode('utf-8')
    ok_message = ('200 OK \n').encode('utf-8')
    fallen_message = ('400 Error: You have fallen \n').encode('utf-8')

    # looks at the user input and moves the user in the specified direction
    # makes sure to store the new position in a temporary variable
    try:
        try:
            new_xcorr, new_ycorr = user.Xcorr, user.Ycorr
        except:
            msg = '400 Error: Could not set new X and Y corrdinate values'
            print(msg)
            msg_to_client = msg.encode('utf-8')
            client.sendall(msg_to_client)
            return msg

        if direction == 'north' or direction == 'up' or direction == 'w':
            new_xcorr -= 1
        elif direction == 'south' or direction == 'down' or direction == 's':
            new_xcorr += 1
        elif direction == 'east' or direction == 'right' or direction == 'd':
            new_ycorr += 1
        elif direction == 'west' or direction == 'left' or direction == 'a':
            new_ycorr -= 1
        else:
            raise ValueError('Invalid Input')

        # Runs the collision function to see if the user collided with a wall or fallen

        check = collision(User('username', 0, new_xcorr, new_ycorr, 0, 0, 0, False))
        match check:
            case 1:
                # No collision, update the user's position
                user.Xcorr = new_xcorr
                user.Ycorr = new_ycorr
                client.sendall(ok_message)
                return '200 OK'
            case 0:
                # Collision, send an error message to the user
                client.sendall(collision_message)
                return '400 Error: Collision'
            case -1:
                # The user has fallen, send an error message to the user
                # Remove the user from the UserList
                fallen_message = '400 Error: You have fallen\n'.encode('utf-8')
                client.sendall(fallen_message)
                user.Fallen = True
                print('User has fallen')
                return '400 Error: You have fallen\n'

    except ValueError:
        error_message = '400 Error: Invalid Input\n'.encode('utf-8')
        client.sendall(error_message)
        return '400 Error: Invalid Input'


def leaderboard_command(client) -> str:
    """Sends a leaderboard to all clients containing the usernames and scores of all users

    Args:
        client (client): Is the client socket used to send messages

    Returns:
        str: Returns a success code '200' if the leaderboard was sent successfully
        Returns '400' an error code if the leaderboard was not sent successfully
    """
    leaderboard = []

    # Update the players scores, adds them to the leaderboard
    # Sends the leaderboard to the client
    for player in UserList:
        if player.Fallen is not True:
            player.Score = round(calculate_Score(player), 2)

    for player in UserList:
        leaderboard.append(player.Username + ' ' + str(player.Score))

    if leaderboard:
        message = ('200 Player: ' + ', '.join(leaderboard) + "\n").encode('utf-8')
        client.sendall(message)
        return message.decode('utf-8')
    error_message = '400 Error: No players in the leaderboard\n'.encode('utf-8')
    client.sendall(error_message)
    return error_message.decode('utf-8')


def chatbox_command(message, client) -> str:
    """Works as a global chat for the game
        Users can input a message and it is broadcasted to all users

    Args:
        message (string): The message the user wants to send

    Returns:
        str: Returns a success code '200' if the message was sent successfully
        Returns '400' an error code if the message was not sent successfully
    """
    # send a message to all players
    username = getUsername(client)
    chat = ('MSG ' + username + ':' + message + '\n').encode('utf-8')

    try:
        for player in UserList:
            try:
                player.Address.sendall(chat)
            except BrokenPipeError:
                # Handle the BrokenPipeError (client disconnected)
                print(f"Error: Broken pipe. User {player.Username} disconnected.")
    except TypeError as e:
        print(f"Error while sending chat message: {e}")
        return '400 Error'

    return '200 OK\n'


def info_command(client) -> str:
    """Sends the current game information to the client

    Args:
        client (client): Is the client socket used to send messages

    Returns:
        str: Returns a success code '200' if the game information was sent successfully
    """
    time = round(game_info(), 2)
    message = ('200 INFO OK ' + str(time) + ' Seconds, ' + str(
        len(UserList)) + ' Users Active,  The Minecraft Experience \n').encode('utf-8')
    client.sendall(message)
    return '200 OK'


def player_update(client) -> str:
    """Sends the current player information to the server

    Args:
        client (client): Is the client socket used to send messages and get the user

    Returns:
        str: Returns a message containing the player information
    """
    # example 200 PLAYER name, xcorr, ycorr, score, fallen
    message = ('200 PLAYER ' + str(get_user(client).Username) + ' '
               + str(get_user(client).Xcorr) + ' ' + str(get_user(client).Ycorr)
               + ' ' + str(get_user(client).Score)).encode('utf-8')
    return message.decode('utf-8')
