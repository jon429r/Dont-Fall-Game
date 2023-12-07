##DONE
##OtherCommands.py

from User import UserList


def parse_input(data):
    """Parses the input data.

    The parse input function takes the data received from the client and splits it into a list
    of strings. The list is then returned.

    Args:
        data (_type_): Input data from client.

    Returns:
        A list of strings.
    """
    data = data.split()
    return data

def username_command(username) -> bool:
    """Checks if the username is available.

    Args:
        username (str): The username to be checked.

    Returns:
        boolean: True if the username is available, False if it is not.
    """
   
    if any(user.Username == username for user in UserList):
        print(UserList)
        return False  # Username is already taken
    else:
        return True   # Username is available
