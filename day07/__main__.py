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

seeking = "shiny gold"

# We first have to iterate through all of the input lines and create
# a mapping to describe what each bag contains
bags = dict()
for line in inputLines:
    if not len(line.strip()):
        continue
    bagName, contentsLine = re.match(
        r"^(.*?) bags contain (.*)$", line.strip()
    ).groups()
    contents = re.findall(r"(\d+) (.*?) bags?", contentsLine)
    bags[bagName] = {name: int(count) for count, name in contents}


# Method to recursively find contents of a bag
def getBagNamesWithin(name):
    bagNames = set()
    bagNames.add(name)
    contents = bags[name]
    for bagName in contents:
        bagNames = bagNames.union(getBagNamesWithin(bagName))
    return bagNames


# Answer for part 1 is the number of bag colors that eventually contain
# a shiny gold bag
found = sum(
    [
        int(seeking in getBagNamesWithin(bagName))
        for bagName in bags
        if bagName != seeking
    ]
)
print(f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {found}")


# Method to recursively find contents of a bag
def countBagContents(name):
    count = 1
    contents = bags[name]
    for bagName, bagCount in contents.items():
        count += bagCount * countBagContents(bagName)
    return count


# Answer for part 2 is the number of bags contained within a single
# shiny gold bag. We subtract 1 to account for the gold bag itself.
print(
    f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {countBagContents(seeking) - 1}"
)
