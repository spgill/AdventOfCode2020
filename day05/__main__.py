# stdlib imports
import itertools
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

# Strip newline characters from the lines
inputLines = [line.strip() for line in inputLines]

# Iterate over each line, each of which is a "boarding pass", and
# parse the "seat id" for each one.
seatIds = []
for line in inputLines:
    seatIds.append(
        int(
            line.replace("F", "0")
            .replace("B", "1")
            .replace("L", "0")
            .replace("R", "1"),
            2,
        )
    )

# The answer to part 1 is the highest seat ID
print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {max(seatIds)}")

# The answer to part 2 is the ID in the middle of three consecutive ID's
for idList in itertools.combinations(seatIds, 2):
    sortedList = sorted(idList)
    if sortedList[1] == sortedList[0] + 2:
        middleId = sortedList[0] + 1
        if middleId not in seatIds:
            print(f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {middleId}")
