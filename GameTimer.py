##DONE
##GameTimer.py
import socket
import time

game_timer: float = None
game_over: bool = True

def start_game_timer():
    """Called when the game starts to start the game timer
    """
    try:
        global game_timer, game_over
        game_timer = time.time()
        game_over = False
        print("Game Timer Started")
    except:
        print('Error starting game timer')

def map_update_timer():
    """Called when the game starts to start the map update timer
        Runs the map command every second
    """
    from User import UserList
    interval_seconds = 1
    try:
        while True:
            if len(UserList) is not 0:
                from Map import map_command
                map_command(False)
            else:
                print('No Users in UserList')
                pass
            time.sleep(interval_seconds)
    except socket.error as e:
        print(f'Error in map_update_timer function: {e}')



def game_info():
    """Returns the game timer and game over status
        Also called to calculate the elapsed time to adjust the scores

    Returns:
        float: Returns the game timer
        bool: Returns the game over status
    """
    try:
        if game_timer and not game_over:
            elapsed_time = time.time() - game_timer
        else:
            elapsed_time = 0

        return elapsed_time
    except:
        print('error in game info function')
