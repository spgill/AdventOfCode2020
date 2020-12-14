# stdlib imports
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
inputGroups = inputHandle.read().split("\n\n")

abet = set("abcdefghijklmnopqrstuvwxyz")


# Iterate through the groups and the unique number of letters for each
# person in each group. Part 1 is finding the unique answers for anyone
# in a group (union). Part 2 is finding the unique answers that
# everyone gave (intersection).
totalP1, totalP2 = 0, 0
for group in inputGroups:
    anyone = set()
    everyone = abet

    for line in group.strip().split("\n"):
        unique = set()
        for char in line:
            if char in abet:
                unique.add(char)
        anyone = anyone.union(unique)
        everyone = everyone.intersection(unique)

    totalP1 += len(anyone)
    totalP2 += len(everyone)

print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {totalP1}")
print(f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {totalP2}")
