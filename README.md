# Don't Fall Game

## Overview

Welcome to the Don't Fall Game, a top-down two-dimensional game designed to showcase my skills in building servers and clients within Python. The server is a TCP server connected to by the client over a local host connection by default. The IP address and PORT can be adjusted to fit the user's personal needs.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Gameplay Screenshots](#gameplay-screenshots)
- [Technical Details](#technical-details)
  - [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

The server and client were developed by me and include adequate error handling specifically for this application.

## Getting Started

1. Clone the GitHub repository.
2. Install the prerequisites by running the `install_prerequisites.py` script.
3. Run the server using the command `python3 server.py`.
4. Run the client using the command `python3 client.py`.

### Prerequisites

- Pygame

## How to Play

The objective of the game is to avoid falling into the lava as tiles randomly fall around you. Navigate using the buttons in a D-pad formation. 
To bring up the global chat, press '/' and type your message. Then press Enter to send the message. This is broadcasted to all players.

## Gameplay Screenshots

Include screenshots or images showcasing the gameplay, graphics, and the overall visual experience of your game.

## Technical Details

This program is written in Python using the Socket library.

### Built With

- Python 3.10.10
- Socket
- Threading
- Pygame
