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
adapters = sorted([int(s.strip()) for s in inputLines if s.strip()])

# Your device joltage is the highest adapter joltage, plus three
# Add this to the adapters list
deviceJoltage = max(adapters) + 3
adapters.append(deviceJoltage)

# For part 1 we have to go through the list of adapters and pick ones adjust
# our cumulative joltage by the smallest amount until all adapters are
# accounted for. We include the device joltage in this list.
adapterCount = [0, 0, 0]
adapterSet = set(adapters)
joltage = 0
while True:
    found = False
    for i in range(3):
        seeking = joltage + i + 1
        if seeking in adapterSet:
            adapterSet.remove(seeking)
            joltage = seeking
            adapterCount[i] += 1
            found = True
            break
    if not found:
        break

# Answer to part one is the *product* of 1-joltage and 3-joltage adapters
print(
    f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {adapterCount[0] * adapterCount[2]}"
)


# The goal of part 2 is to count ALL the possible (valid) combinations of
# adapters between outlet and device. I originally tried to brute force
# computer each combination, but that was a (literal) waste of time.
memory = {0: 1}
for joltage in adapters:
    memory[joltage] = (
        memory.get(joltage - 3, 0)
        + memory.get(joltage - 2, 0)
        + memory.get(joltage - 1, 0)
    )
print(f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {memory[deviceJoltage]}")
