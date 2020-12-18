# stdlib imports
import math
import pathlib
import sys

# vendor imports
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

# Open input file
if len(sys.argv) < 2:
    print(f"{Fore.RED}No input file given{Style.RESET_ALL}")
    exit()
inputPath = pathlib.Path(sys.argv[1])
if not inputPath.exists():
    print(f"{Fore.RED}Input file does not exist{Style.RESET_ALL}")
    exit()
inputHandle = inputPath.open("r")
inputLines = inputHandle.readlines()

# Parse the input lines into a list of instructions
instructions = list()
for line in inputLines:
    line = line.strip()
    if not len(line):
        continue
    op = line[0]
    arg = line[1:]
    instructions.append([op, int(arg)])

# For part 1, we simulate the ship's movements through every instruction
# using the simple instruction set
x = 0
y = 0
angle = 0
for op, arg in instructions:
    if op == "N":
        y -= arg
    elif op == "S":
        y += arg
    elif op == "E":
        x += arg
    elif op == "W":
        x -= arg
    elif op == "L":
        angle -= math.radians(arg)
    elif op == "R":
        angle += math.radians(arg)
    elif op == "F":
        x += round(math.cos(angle)) * arg
        y += round(math.sin(angle)) * arg

# The answer to part 1 is the sum of the manhattan distance from origin
print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {abs(x) + abs(y)}")

# For part 2, we do the same but use the more complicated waypoint set
shipX = 0
shipY = 0
waypointX = 10
waypointY = -1
waypointAngle = 0
for op, arg in instructions:
    if op == "N":
        waypointY -= arg
    elif op == "S":
        waypointY += arg
    elif op == "E":
        waypointX += arg
    elif op == "W":
        waypointX -= arg
    elif op in ["L", "R"]:
        if op == "L":
            arg = -arg
        newX = (
            round(math.cos(math.radians(arg))) * waypointX
            - round(math.sin(math.radians(arg))) * waypointY
        )
        newY = (
            round(math.sin(math.radians(arg))) * waypointX
            + round(math.cos(math.radians(arg))) * waypointY
        )
        waypointX, waypointY = newX, newY
    elif op == "F":
        shipX += waypointX * arg
        shipY += waypointY * arg

# The answer to part 2 is the sum of the ship's manhattan distance from origin
print(f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {abs(shipX) + abs(shipY)}")
