import subprocess
import sys

def check_and_install(command, install_command, message):
    try:
        subprocess.check_output(command, shell=True)
        print(f"{message} is already installed.")
    except subprocess.CalledProcessError:
        print(f"{message} not found. Installing {message}...")
        subprocess.run(install_command, shell=True)
        print(f"{message} installed.")

def main():
    # Check and install Python
    check_and_install("python --version", "", "Python")

    # Check and install pip
    check_and_install("pip --version", "python -m ensurepip --default-pip", "pip")

    # Install Pygame
    print("Installing Pygame...")
    subprocess.run("pip install pygame", shell=True)
    print("Pygame installed.")

    print("Installation complete.")

if __name__ == "__main__":
    main()
