##DONE
##User.py

from GameTimer import game_info
## List of users
UserList = []

class User:
    """User class to keep track of user information
    """
    def __init__(self, Username, Address, Xcorr, Ycorr, StartTime, EndTime=None, Score=None, Fallen=None):
        self.Username = Username
        self.Address = Address
        self.Xcorr = Xcorr
        self.Ycorr = Ycorr
        self.StartTime = StartTime
        self.EndTime = EndTime if EndTime is not None else game_info()  # Use provided EndTime or game_info()
        self.Score = round(calculate_Score(self), 2)
        self.Fallen = Fallen

    def display_user_info(self):
        """
        Display the user's information.
        """
        print(f"Username: {self.Username}")
        print(f"Address: {self.Address}")
        print(f"Location: {self.Xcorr}, {self.Ycorr}")
        print(f"Score: {self.Score}")

def getID() -> str:
    """Generates a unique ID for each user

    Returns:
        string: A unique ID for each user
    """
    player_id = len(UserList)
    userID = 'User' + str(player_id)
    return userID

def get_user(client):
    """Gets the user object from the client

    Args:
        client (client): The client object

    Returns: User object
    """
    ##loops through userlist searching for the user object 
    ##with the same address as the client
    for user in UserList:
        if user.Address == client:
            return user
    return None

def get_Xcorr(client):
    """Gets the X coordinate from the client

    Args:
        client (client): The client object

    Returns: X coordinate
    """
    ##loops through userlist searching for the user object
    for user in UserList:
        if user.Username == client:
            return user.Xcorr
    return None

def get_Ycorr(client):
    """Gets the Y coordinate from the client

    Args:
        client (client): The client object

    Returns:
        user: Y coordinate
    """
    for user in UserList:
        if user.Username == client:
            return user.Ycorr
    return None

def get_Fallen(client):
    for user in UserList:
        if user.Username == client:
            return user.Fallen
    return None

def get_Score(user):
    """Gets the score from the user object

    Args:
        user (User): The user object

    Returns:
        User: The score of the user
    """
    ##Uses the start time and gets the current time to calculate the score
    try:
        Score = user.EndTime - user.StartTime
        return Score
    except KeyError:
        return None  # Handle KeyError appropriately

def calculate_Score(user):
    """Calculates the score of the user

    Args:
        user (User): The user object

    Returns:
        Int: The score of the user
    """
    user.EndTime = game_info()
    try:
        Score = user.EndTime - user.StartTime
    except TypeError:  # Handle TypeError if StartTime or EndTime is not valid
        Score = 0
    Score = max(0, Score)  # Score cannot be negative
    return Score

def getUsername(client):
    for user in UserList:
        if user.Address == client:
            return user.Username
    return None