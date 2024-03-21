"""christopher_rockett_final_project.py - A Maze Game For User to play.

This file uses conditions, loops, three collection types and all the other
final project requirements to create a Motorcycle Maze Game. The user is
riding a motorcycle which they control using the arrow keys to escape the maze
they choose in ther terminal. There are square boundaries for that outline
a maze. Once the user gets to the end of the maze, a completion message pops
up and a file containing their coordinate list is saved.

Christopher Rockett
Final Project
"""
# Importing all necessary libraries.
import turtle as t
import tkinter as tk
from tkinter import messagebox


class LongInputException(Exception):
    """User-defined exception to use in the starting menu."""

    def __init__(self, length, atleast):
        """Initialize exception to stay consistent with other exceptions."""
        super().__init__()
        self.length = length
        self.atleast = atleast


MAX_LENGTH = 2

# Menu for user to choose difficulty.
choice = ""
while True:
    try:
        choice = input("Which Difficulty Level?:\n1. Easy\n2. Medium\n3. Hard"
                       + "\n4. Quit\n-> ")
        if len(choice) > MAX_LENGTH:
            raise LongInputException(len(choice), MAX_LENGTH)
    # Stops CTRL D / CTRL Z Errors.
    except EOFError:
        print("Please don't EOF me.")
    # Stops CTRL C Errors.
    except KeyboardInterrupt:
        print("You cancelled the operation.")
    # Sets map based on user's choice.
    else:
        if choice == "1":
            diffculty = 1
            break
        elif choice == "2":
            diffculty = 2
            break
        elif choice == "3":
            difficulty = 3
            break
        elif choice == "4":
            break

# Creates a turtle window with initial settings.
screen = t.Screen()
screen.screensize(1000, 1000)
screen.bgcolor('black')
screen.title('Motorcycle Maze Craze')


class Elements:
    """Sets a parent class for all turtles used in program."""

    def __init__(self):
        """Set variables and speed for turtle."""
        self.pen = t.Turtle()
        self.pen.speed(0)
        self.pen.penup()


class Player(Elements):
    """Set up player on GUI and initializes movement functions."""

    def __init__(self):
        """Initialize values not already set by parent class for turtle."""
        super().__init__()
        self.pen.shape('circle')
        self.pen.color('blue')

    def check_win(self):
        """Check to see if player beat the maze map using coordinates."""
        if player.pen.pos() == (275, -300):
            # Window pop-up letting user know they've won.
            messagebox.showinfo("Motorcycle Maze Craze", "YOU WON!! "
                                + "Congratulations!")
            # Creates a file to track all of player's movements.
            with open('route.txt', 'w') as f:
                for line in movement:
                    f.write("%s\n" % line)

    def up(self):
        """Turtle moves up when called."""
        # Gathers player turtle positions.
        x_cord = player.pen.xcor()
        y_cord = player.pen.ycor()

        # Restricts turtle from going through walls.
        if (x_cord, y_cord + 25.00) not in walls:
            self.pen.setheading(90)
            self.pen.forward(25)
            # Shows current coordinates in terminal.
            print(COORDINATES)

            # Adds movement to output file and checks for a win.
            movement.append(str(player.pen.pos()))
            self.check_win()

    def down(self):
        """Turtle moves down when called."""
        # Gathers player turtle positions.
        x_cord = player.pen.xcor()
        y_cord = player.pen.ycor()

        # Restricts turtle from going through walls.
        if (x_cord, y_cord - 25) not in walls:
            self.pen.setheading(270)
            self.pen.forward(25)
            # Shows current coordinates in terminal.
            print(COORDINATES)

            # Adds movement to output file and checks for a win.
            movement.append(str(player.pen.pos()))
            self.check_win()

    def left(self):
        """Turtle moves left when called."""
        # Gathers player turtle positions.
        x_cord = player.pen.xcor()
        y_cord = player.pen.ycor()

        # Restricts turtle from going through walls.
        if (x_cord - 25, y_cord) not in walls:
            self.pen.setheading(180)
            self.pen.forward(25)
            # Shows current coordinates in terminal.
            print(COORDINATES)

            # Adds movement to output file and checks for a win.
            movement.append(str(player.pen.pos()))
            self.check_win()

    def right(self):
        """Turtle moves right when called."""
        # Gathers player turtle positions.
        x_cord = player.pen.xcor()
        y_cord = player.pen.ycor()
        # Shows current coordinates in terminal.
        print(COORDINATES)

        # Restricts turtle from going through walls.
        if (x_cord + 25, y_cord) not in walls:
            self.pen.setheading(0)
            self.pen.forward(25)

            # Adds movement to output file and checks for a win.
            movement.append(str(player.pen.pos()))
            self.check_win()


class Map(Elements):
    """Create map using a turtle to visually see on GUI."""

    def __init__(self, map_list):
        """Initialize values not already set by parent class."""
        super().__init__()
        self.pen.shape('square')
        self.pen.color('white')

        # Creates list for map data to store in.
        self.maps = [""]
        self.map_1 = map_list
        self.maps.append(self.map_1)

    def setup_map(self, map, player):
        """Set map up into white squares of even sizes."""
        # Creates Loop to create a grid from text.
        for y in range(len(map)):
            for x in range(len(map[y])):
                character = map[y][x]
                screen_x = -300 + (x*25)
                screen_y = 300 - (y*25)

                # Uses variable x to create walls in text.
                if character == "x":
                    self.pen.goto(screen_x, screen_y)
                    self.pen.stamp()
                    walls.append((screen_x, screen_y))

                # Uses variable p for player starting position in text.
                if character == "p":
                    player.pen.goto(screen_x, screen_y)

    def solve_maze(self, x, y):
        """Determine if maze is solvable."""
        # Exit coordinate of the mazes
        if (x, y) == (275, -300):
            return True

        # False value if ending coordnites is in walls or has been visited.
        if (x, y) in walls or (x, y) in visited:
            return False

        # Checking if route has already been taken.
        visited.add((x, y))

        # Creates directions for algorithm to go in maze.
        directions = [(0, 25), (0, -25), (25, 0), (-25, 0)]
        for dx, dy in directions:
            if self.solve_maze(x + dx, y + dy):
                return True

        # Removes coordinate from list when it backtracks.
        visited.remove((x, y))
        return False


# Creating collections to store data in.
map_list = []
walls = []
movement = []
visited = set()
map_choice = {"1": "map.txt", "2": "map_2.txt", "3": "map_3.txt"}

# Transfers data from file to code from choice made in menu.
with open(map_choice[choice]) as file:
    for line in file:
        map_list.append(line.rstrip())

# Variables for classes and creates map from file to GUI.
player = Player()
generate = Map(map_list)
generate.setup_map(generate.maps[1], player)

COORDINATES = (player.pen.pos())

# Sets hotkeys for turtle to listen and react to.
t.listen()
t.onkey(player.up, "Up")
t.onkey(player.down, "Down")
t.onkey(player.left, "Left")
t.onkey(player.right, "Right")
screen.update()

# Statement that prints whether there is a solution or not.
if generate.solve_maze(-275, 275):
    print("Solution found!")
else:
    print("No solution found.")

# Keeps Turtle window open.
if __name__ == '__main__':
    screen.mainloop()
