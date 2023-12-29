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
2. If python is installed on the device, install the prerequisites by running the `install_prerequisites.py` script.
2. If python3 is not installed, install the prerequisites by typing
`chmod +x install_prerequisites.sh` then `.\install_prerequisites.sh`
3. Run the server using the command `python3 server.py`.
4. Run the client using the command `python3 client.py`.

### Prerequisites

- Pygame coded in 2.5.2
- Python 3.6 or newer

## How to Play

The objective of the game is to avoid falling into the lava as tiles randomly fall around you. Navigate using the buttons in a D-pad formation. 
To bring up the global chat, press '/' and type your message. Then press Enter to send the message. This is broadcasted to all players.

## Gameplay Screenshots

<img width="1274" alt="Screenshot 2023-12-28 at 8 48 38 PM" src="https://github.com/jon429r/Dont-Fall-Game/assets/103213920/f8da9c4a-96a0-4013-9bfe-31dae137af48">


<img width="1274" alt="Screenshot 2023-12-28 at 8 48 08 PM" src="https://github.com/jon429r/Dont-Fall-Game/assets/103213920/c6e446d2-8340-4e0e-bc59-a6ee9ac54db2">


<img width="1273" alt="Screenshot 2023-12-28 at 8 47 30 PM" src="https://github.com/jon429r/Dont-Fall-Game/assets/103213920/75d58b33-d3bd-4bee-ad5c-752df1b10f27">


## Technical Details

This program is written in Python using the Socket library. Graphics draw by me and displayed using Pygame

### Built With

- Python 3.10.10
- Socket
- Threading
- Pygame
