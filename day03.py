# stdlib imports
import functools
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

# Trim newline characters from all of the input lines
inputLines = [line.strip() for line in inputLines]


# Function to retrieve the value in a particular position,
# circularizing the line's pattern
def getCoord(x, y):
    line = inputLines[y]
    return line[x % len(line)]


# For both parts we will be counting trees in the path of a slope
counts = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for slopeX, slopeY in slopes:
    x = 0
    y = 0
    trees = 0
    while y < len(inputLines):
        if getCoord(x, y) == "#":
            trees += 1
        x += slopeX
        y += slopeY

    counts.append(trees)

    # The answer for part 1 is the count of a particular slope
    if slopeX == 3 and slopeY == 1:
        print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {trees}")

# The answer for part 2 is the product of all slope counts
product = functools.reduce(lambda a, b: a * b, counts)
print(f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {product}")
