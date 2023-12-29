import pygame
import socket
import sys
import os

# Setup pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
fps = 60
clock = pygame.time.Clock()
in_game_loop = False

# Connect to the server
Server_Address = '127.0.0.1'
Port = 2042

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((Server_Address, Port))
    print(f'Trying to connect to {Server_Address} at port {Port}')
except socket.error as e:
    print(f"Could not connect to server {e}")

print('Connected')

# Load background image, tile images, and sprite image
print('Importing sprites')
Sprites = {
    'Background_image': '../Sprites/Background.png',
    'snake': '../Sprites/player_sprite.png',
    'tile_image1': '../Sprites/tile1_sprite.png',
    'tile_image2': '../Sprites/Tile_sprite_2.png',
    'sprite_image1': '../Sprites/Sprite1.webp',
    'blank_tile': '../Sprites/Blank_Tile.png'
}

loaded_sprites = {}

# Get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the absolute path to the background image
background_image_filename = os.path.join(script_dir, '../Sprites/Background.png')

try:
    # Load the background image directly from the Sprites dictionary
    background_image = pygame.image.load(Sprites['Background_image'])
    print(f'Successfully loaded background image: {Sprites["Background_image"]}')
except pygame.error as e:
    print(f'Error loading background image: {e}')
    sys.exit(1)


try:
    for sprite_name, sprite_filename in Sprites.items():
        try:
            # Load each sprite using Pygame
            loaded_sprites[sprite_name] = pygame.image.load(sprite_filename)
            print(f'Successfully loaded sprite: {sprite_name}')
        except pygame.error as e:
            print(f'Error loading sprite {sprite_name}: {e}')
except Exception as ex:
    print(f'Error while loading sprites: {ex}')
    sys.exit(1)

sprite_size = 64
tile_size = 64

# Use the Sprites dictionary directly for the background image
background_image = pygame.image.load(Sprites['Background_image'])


# setup buttons
button_font = pygame.font.Font(None, 40)

black = (0, 0, 0)
white = (255, 255, 255)

button_size = 50
up_button = pygame.Rect(775, 500, button_size, button_size)
down_button = pygame.Rect(775, 600, button_size, button_size)
left_button = pygame.Rect(725, 550, button_size, button_size)
right_button = pygame.Rect(825, 550, button_size, button_size)
quit_button = pygame.Rect(50, 50, button_size, button_size)

button_SRCAL = 128
up_button_surface = pygame.Surface((button_size, button_size), pygame.SRCALPHA)
up_button_surface.fill((255, 255, 255, button_SRCAL))

down_button_surface = pygame.Surface((button_size, button_size), pygame.SRCALPHA)
down_button_surface.fill((255, 255, 255, button_SRCAL))

left_button_surface = pygame.Surface((button_size, button_size), pygame.SRCALPHA)
left_button_surface.fill((255, 255, 255, button_SRCAL))

right_button_surface = pygame.Surface((button_size, button_size), pygame.SRCALPHA)
right_button_surface.fill((255, 255, 255, button_SRCAL))

quit_button_surface = pygame.Surface((button_size, button_size), pygame.SRCALPHA)
quit_button_surface.fill((255, 255, 255, button_SRCAL))


#Chat box
chat_box_width = 300
chat_box_height = 500

chat_x = 1250
chat_y = 600

chat_box_surface = pygame.Surface((chat_box_width, chat_box_height), pygame.SRCALPHA)
chat_box_surface.fill((0, 0, 0, 128))  # Background color with alpha transparency

chat_font_size = 18
chat_font = pygame.font.Font(None, chat_font_size)

chat_text = []

chat_box_position = (chat_x - chat_box_width, chat_y - chat_box_height)
chat_box_rect = pygame.Rect(chat_box_position, (chat_box_width, chat_box_height))


def draw_text_input_box(screen, font, rect, text, max_length):
    pygame.draw.rect(screen, (255, 255, 255), rect, 2)
    text_surface = font.render(text, True, (255, 255, 255))

    # Position the text input at the bottom of the rectangle
    text_rect = text_surface.get_rect(center=(rect.centerx, rect.bottom - 10))

    # Adjust y-position to start at the bottom
    text_rect.y = rect.bottom - text_surface.get_height() - 5

    screen.blit(text_surface, text_rect)

# Helper function to parse map data
def parse_map_data(map_data):
    result = []

    for line in map_data.splitlines():
        # Extract the map part of the data
        if line.startswith('200 Map'):
            map_str = line.split(":")
            line_data = map_str[1].strip()  # Remove leading/trailing whitespaces
            line = list(line_data)

            # Append the map list to the result
            result.append(line)

    return result


# Helper function to draw tiles
def draw_tiles(map_data):
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if (row + col) % 2 == 0:
                if map_data[row][col] == '0':
                    screen.blit(loaded_sprites['tile_image1'], (col * tile_size, row * tile_size))
                elif map_data[row][col] == 'P':
                    screen.blit(loaded_sprites['tile_image1'], (col * tile_size, row * tile_size))
                    screen.blit(loaded_sprites['snake'], (col * sprite_size, row * sprite_size))
                elif map_data[row][col] == 'X':
                    screen.blit(loaded_sprites['blank_tile'], (col * tile_size, row * tile_size))
                else:
                    pass
            else:
                if map_data[row][col] == '0':
                    screen.blit(loaded_sprites['tile_image2'], (col * tile_size, row * tile_size))
                elif map_data[row][col] == 'P':
                    screen.blit(loaded_sprites['tile_image2'], (col * tile_size, row * tile_size))
                    screen.blit(loaded_sprites['snake'], (col * sprite_size, row * sprite_size))
                elif map_data[row][col] == 'X':
                    screen.blit(loaded_sprites['blank_tile'], (col * tile_size, row * tile_size))
                else:
                    pass
import random

def create_random_map(rows, cols):
    game_map = []
    elements = ['X', '0', 'P']
    for row in range(rows):
        map_row = [random.choice(elements) for _ in range(cols)]
        game_map.append(map_row)
    print(game_map)
    return game_map


def display_leaderboard():
    # Send the leaderboard command
    client_socket.sendall('leaderboard'.encode('utf-8'))

    # Receive and decode the leaderboard response
    leaderboard_bytes = client_socket.recv(4096)
    leaderboard_str = leaderboard_bytes.decode('utf-8')
    print(f'Leaderboard: {leaderboard_str}')

    leaderboard = leaderboard_str.split(':')[1]

    # Split the leaderboard into lines
    leaderboard_lines = leaderboard.split(',')

    # Display the leaderboard in the top right corner
    font_size = 40
    font_color = 'pink'
    font = pygame.font.Font(None, font_size)
    x = 950
    y = 10

    for line in leaderboard_lines:
        text = font.render(line, True, font_color)
        screen.blit(text, (x, y))
        y += font_size

# Game loop
chatting = False
chat_input = ""
fallen = False
running = True

def main():
    global running, chat_text, chatting, chat_input, fallen
    print('in main')

    try:
        # Send a message to start the game
        msg = input('Would you like to login or exit')
        msg = msg.encode('utf-8')
        client_socket.sendall(msg)
        print(f'Sent {msg}')

        # Receive the initial message from the server
        msg = client_socket.recv(4096).decode('utf-8')
        print(f'Received message: {msg}')

        if msg.startswith('200 HELLO Ok'):
            running = True
            fallen = False
            print('Starting game loop')
        else:
            running = False
            print('Failed to start game loop. Server response:', msg)

    except socket.error as e:
        print(f"Error: {e}")
        running = False
        print('Game ended by server')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    if event.button == 1:
                        if up_button.collidepoint(event.pos) and fallen is False:
                            print('Move UP')
                            movement = 'up'.encode('utf-8')
                            client_socket.sendall(movement)
                        elif down_button.collidepoint(event.pos) and fallen is False:
                            print('Move Down')
                            movement = 'down'.encode('utf-8')
                            client_socket.sendall(movement)
                        elif left_button.collidepoint(event.pos) and fallen is False:
                            print('Move Left')
                            movement = 'left'.encode('utf-8')
                            client_socket.sendall(movement)
                        elif right_button.collidepoint(event.pos) and fallen is False:
                            print('Move Right')
                            movement = 'right'.encode('utf-8')
                            client_socket.sendall(movement)
                except:
                    print('Error after pressing movement controls')

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SLASH:
                    chatting = True
                elif chatting:
                    if event.key == pygame.K_RETURN:
                        chat_command = 'chat '
                        chat_message = chat_command + chat_input  # Concatenate the command and input
                        encoded_message = chat_message.encode('utf-8')
                        client_socket.sendall(encoded_message)
                        print(f'Player sent: {chat_message}')

                        chat_input = ""
                        chatting = False

                    elif event.key == pygame.K_BACKSPACE:
                        chat_input = chat_input[:-1]
                    elif event.unicode.isprintable():
                        chat_input += event.unicode

        # Receive updates from the server
        data_from_server = client_socket.recv(4096).decode('utf-8')
        print(f'Received data: {data_from_server}')

        if data_from_server.startswith('200 Player:'):
            try:
                display_leaderboard()
            except Exception as ex:
                print(f'Failed to display leaderboard: {ex}')

        elif data_from_server.startswith('400 Error: You have fallen'):
            print('You have fallen. Game over.')
            fallen = True

        elif data_from_server.startswith('MSG'):

            # Extract the message content after 'MSG'
            message_content = data_from_server[3:].strip()
            chat_text.append(message_content)

        elif data_from_server.startswith('200 Map'):
            # Process the received map data
            game_map = parse_map_data(data_from_server)

            if game_map == -1:
                print("Error parsing map data. Exiting.")
                running = False
            else:
                print('Displaying game')
                # Display the map
                screen.fill((0, 0, 0))  # Fill with black color
                screen.blit(loaded_sprites['Background_image'], (0, 0))  # Use the loaded image directly
                draw_tiles(game_map)
                try:
                    screen.blit(up_button_surface, up_button.topleft)
                    screen.blit(down_button_surface, down_button.topleft)
                    screen.blit(left_button_surface, left_button.topleft)
                    screen.blit(right_button_surface, right_button.topleft)
                except:
                    print('failed to draw buttons')

                try:

                    max_length = 100
                    screen.blit(chat_box_surface, chat_box_rect.topleft)

                    # Calculate the position to start rendering chat_text a few pixels above the text input box
                    y_position = chat_box_rect.bottom - 20 - chat_font_size

                    # Render chat_text above the text input box
                    for line in reversed(chat_text):
                        text = chat_font.render(line, True, white)
                        text_rect = text.get_rect(left=chat_box_rect.left + 10, bottom=y_position)
                        screen.blit(text, text_rect)
                        y_position -= chat_font_size

                    # Draw the text input box
                    text_input_rect = pygame.Rect(
                        chat_box_rect.left + 10,
                        chat_box_rect.bottom - 30,
                        chat_box_rect.width - 20,
                        20
                    )
                    draw_text_input_box(screen, chat_font, text_input_rect, chat_input, max_length)

                except:
                    print('Failed to draw chat box')


                if fallen is True:
                    font_size = 200
                    font_color = 'grey'
                    font = pygame.font.Font(None, font_size)

                    text = font.render('You Have Fallen', True, font_color)
                    screen.blit(text, (100, 200))

                pygame.display.flip()

        # Cap the frame rate
        clock.tick(fps)

    print('Quit')
    pygame.quit()

# Run the event loop
if __name__ == "__main__":
    main()
