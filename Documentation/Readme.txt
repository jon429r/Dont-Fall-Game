Readme.txt 

Project Name: The Minecraft Experience

The goal of this project is to host a server that runs a game.
The purpose of this project is to test my backend/server making
skills so the graphical side is not the focus.

By the end the gameplay will be simple. A player connects to the server
The server is started by running the Server.py file and has config arguements
PORT and MAPSIZE.

Run the server by running the Server.py file EX: `python3 Server.py -p 2042

Connect to the server using your favorite client
This is tested in telnet EX: telnet localhost 2042

I use telnet to connect, the IP address is 127.0.0.1 on PORT number 2042 by default
A player logs in with the hello command followed by a username
and the game plays when the user enters.

List of commands that the user can run:
Hello <Username>

-Can only be run at the start to log the user in
-All other commands are locked besides quit until the user runs this command

Quit

-The user quits the server

north, up, w
south, down, s
east, right, d
west, left, a

-The user moves in these directions
-Up, down, right, left

map

-The map is displayed
-The map displays every second by default
-This command can be used to call the map manually

leaderboard

-The leaderboard is displayed: Displays the username of all players followed
by the scores, top scores at the top in decending order

chatbox <Message>

-Sends the message to all players in the server

info

-Displays information about the server
< 200 INFO <clock>,<player count>,<name of game>


For Details on all the files see CodeInfo.txt
