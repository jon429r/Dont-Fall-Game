##DONE
##Physics.py

from Tile import FallenTiles

def collision(player) -> int:
    """Checks if the player is within the map boundaries 
    and if the player is trying to move to a fallen tile

    Args:
        player (User): The user object of the player

    Returns:
        _type_: Returns 1 if there is no collision, 
        0 if there is a collision, 
        and -1 if the player has fallen
    """
    map_width = 19 
    map_height = 9 

    Fallen = collision_tile(player)
    if Fallen:
        return -1
    ## Check if the player is within the map boundaries
    if 0 <= player.Xcorr < map_width and 0 <= player.Ycorr < map_height:
        return 1  ## No collision, the player is within the map boundaries
    else:
        return 0  ## Collision, the player is outside the map boundaries

def collision_tile(player) -> bool:
    """Checks if the player is trying to move to a fallen tile

    Args:
        player (User): The user object of the player

    Returns:
        boolean: Returns True if there is a collision,
    """
    for tile in FallenTiles:
        if player.Xcorr == tile.Xcorr and player.Ycorr == tile.Ycorr:
            return True  ## Collision, the player is trying to move to a fallen tile
    return False  ## No collision, the player is not trying to move to a fallen tile
