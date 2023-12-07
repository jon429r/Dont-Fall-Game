##DONE
##Tile.py

import random

board_width = 10
board_height = 10


class Tile:
    """Tile class to keep track of fallen tiles
    """
    def __init__(self, x, y):
        self.Xcorr = x
        self.Ycorr = y

## List of fallen tiles
FallenTiles = []
## List of remaining tiles
RemainingTiles = [Tile(-1, -1) for _ in range(board_width * board_height)]

def fall(DEFAULT_MAP):
    """Randomly selects a tile to fall 1-3 can fall at a time
        adds the tile to the list of fallen tiles
        places the tile in the DEFAULT_MAP on a spot with '0'

    Args:
        DEFAULT_MAP (Any): The map that the tiles will fall on
    """
    global FallenTiles, RemainingTiles

    rand = random.randint(1, 3)
    print(f'Number of fallen tiles: {len(FallenTiles)}')
    print(f'Number of remaining tiles: {len(RemainingTiles)}')

    ## Randomly select tiles to fall
    for i in range(rand):
        if RemainingTiles:
            tile = random.choice(RemainingTiles)
            FallenTiles.append(tile)
            RemainingTiles.remove(tile)

            # Find a random position with '0' in DEFAULT_MAP
            positions = [(x, y) for x in range(len(DEFAULT_MAP)) for y in range(len(DEFAULT_MAP[0])) if
                         DEFAULT_MAP[x][y] == '0']

            # Place the tile in DEFAULT_MAP
            if positions:
                x, y = random.choice(positions)
                DEFAULT_MAP[x][y] = 'X'
                tile.Xcorr, tile.Ycorr = x, y

        else:
            from Map import map_command
            FallenTiles = []
            RemainingTiles = [Tile(-1, -1) for _ in range(board_width * board_height)]
            map_command(True)

def clear_fallen_tiles():
    print('clearing fallen tiles')
    try:
        Tile.FallenTiles = []
        Tile.RemainingTiles = [Tile(-1, -1) for _ in range(board_width * board_height)]
        print('game board reset')
    except Exception as e:
        print(f'Error clearing fallen tiles: {e}')
