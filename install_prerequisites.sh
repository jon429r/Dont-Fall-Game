#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
else
    echo "Python not found. Installing Python..."
    # Install Python on Windows
    if [ "$(uname)" == "Darwin" ]; then
        brew install python3
    elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
        sudo apt-get update
        sudo apt-get install python3
    else
        echo "Unsupported operating system."
        exit 1
    fi
fi

# Check if pip is installed
if command -v pip3 &>/dev/null; then
    echo "pip is already installed."
else
    echo "pip not found. Installing pip..."
    python3 -m ensurepip --default-pip
fi

# Install Pygame
echo "Installing Pygame..."
pip3 install pygame

echo "Installation complete."