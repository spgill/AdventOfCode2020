# stdlib imports
import pathlib
import re
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

pattern = re.compile(r"(\d+)-(\d+) (\w): (.*)")

# For part 1, we are checking each line valid ranges of counts of a
# specified letter.
validP1 = 0
for line in inputLines:
    (minCount, maxCount, letter, passwd) = pattern.match(line).groups()
    letterCount = passwd.count(letter)
    if int(minCount) <= letterCount <= int(maxCount):
        validP1 += 1

print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {validP1}")

# For part 2, we are checking for specified character in one of two indexes.
# We use the XOR operator below because only 1 position can have the
# character.
validP2 = 0
for line in inputLines:
    (index1, index2, letter, passwd) = pattern.match(line).groups()
    char1 = passwd[int(index1) - 1]
    char2 = passwd[int(index2) - 1]
    if (char1 == letter) ^ (char2 == letter):
        validP2 += 1

print(f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {validP2}")
