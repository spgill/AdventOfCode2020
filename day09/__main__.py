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
inputLines = inputHandle.readlines()

# Parse the input lines into numbers
values = [int(s.strip()) for s in inputLines if s.strip()]

# Iterate through every line (after 25) and check if the number is the
# sum of two of the previous 25 numbers
invalid = 0
preamble = 25
i = preamble
while i < len(inputLines):
    current = values[i]
    previous = values[i - preamble : i]

    valid = False
    for n in previous:
        if (current - n) in previous:
            valid = True
            break

    # If not valid, this is the invalid number we will be seeking in part 2
    if not valid:
        invalid = current
        break

    i += 1

# The invalid number is also the answer to part 1
print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {current}")

# For part 2, look for a contiguous section that adds up to the "invalid"
# number found in part 1.
contiguousLength = 2
correctSet = None
while not correctSet:
    i = contiguousLength
    while i < len(inputLines):
        contiguousSet = values[i - contiguousLength : i]
        if sum(contiguousSet) == invalid:
            correctSet = sorted(contiguousSet)
            break
        i += 1
    contiguousLength += 1

# The answer is then the sum of the smallest and largest numbers of this
# contiguous set.
print(
    f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {correctSet[0] + correctSet[-1]}"
)
