# stdlib imports
import itertools
import pathlib
import sys

# vendor imports
import colorama
from colorama import Fore, Back, Style

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

lines = input

# Part 1, Combine all of the input lines until you find one that sums to 2020
for a, b in itertools.combinations(inputLines, 2):
    a = int(a)
    b = int(b)
    if a + b == 2020:
        print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {a * b}")

# Part 2, the same thing but with three entries
for a, b, c in itertools.combinations(inputLines, 3):
    a = int(a)
    b = int(b)
    c = int(c)
    if (a + b + c) == 2020:
        print(f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {a * b * c}")