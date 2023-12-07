##DONE
##Map.py

from User import UserList, get_Fallen
from Tile import FallenTiles, fall, clear_fallen_tiles

width = 10
height = 10


Empty_Map = [["0" for x in range(width)] for y in range(height)]
Game_Map = [["0" for j in range(width)] for k in range(height)]

def map_command(create_new_map)->str:
    """Displays the game map for the user and sends it to all connected clients.

    Args: create_new_map: Bool
    passed in to see if the map must be reset because it was full

    Returns:
        str: Returns a success code '200' if the map was sent successfully
    """
    global height, width

    DEFAULT_MAP = [["0" for x in range(width)] for y in range(height)]

    ## Update map with player positions and X for fallen tiles the user cannot go on
    for user in UserList:
        if user.Xcorr >= 0 and user.Ycorr >= 0 and not user.Fallen:
            DEFAULT_MAP[user.Xcorr][user.Ycorr] = 'P'

    fall(DEFAULT_MAP)

    if create_new_map:
        clear_fallen_tiles()

    for tile in FallenTiles:
        if tile.Xcorr >= 0 and tile.Ycorr >= 0:
            DEFAULT_MAP[tile.Xcorr][tile.Ycorr] = 'X'

    send_map(DEFAULT_MAP)
    return '200'

def send_map(DEFAULT_MAP):

    ## Send the map to all connected clients
    for recipient in UserList:
        try:
            recipient.Address.sendall(create_map_message(DEFAULT_MAP))
        except:
            print(f'error trying to send the map to: {recipient}')
            # remove the user from the userlist because they probably disconnected
            UserList.remove(recipient)
            print(f'Removing {recipient} from UserList, Sending map again')
            send_map(DEFAULT_MAP)


def create_map_message(game_map):
    """Creates a message format for the game map.

    Args:
        game_map (list): The 2D list representing the game map.

    Returns:
        str: Formatted message for the game map.
    """
    map_message = ""
    index = 0
    for row in game_map:
        row_string = "200 Map 00" + str(index) + ": " + '' .join(map(str, row)) + "\n"
        index = index + 1
        map_message += row_string
    map_message += "\n"

    print(map_message)
    return map_message.encode('utf-8')
