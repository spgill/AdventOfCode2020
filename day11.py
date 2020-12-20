# stdlib imports
import copy
import enum
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


# Enum class representing the values for seat map tiles
class Tile(enum.Enum):
    EmptySeat = "L"
    OccupiedSeat = "#"
    Floor = "."
    OOB = "?"  # Out Of Bounds


# Class to represent a single grid object
class SimpleGrid:
    adjacentRange = [-1, 0, 1]
    occupiedTolerance = 4

    def __init__(self, data):
        self.data = copy.deepcopy(data)

    # Create a copy of the grid
    def copy(self):
        return copy.deepcopy(self)

    # Serialize grid into a string for comparison
    def serialize(self):
        return "\n".join(["".join([x.value for x in y]) for y in self.data])

    # Return the x, y size of the grid
    def gridSize(self):
        return (len(self.data[0]), len(self.data))

    # Function to retrieve tile at coords. Is aware of boundaries.
    def getTile(self, x, y):
        if y >= len(self.data) or y < 0:
            return Tile.OOB
        row = self.data[y]
        if x >= len(row) or x < 0:
            return Tile.OOB
        return Tile(row[x])

    # Set tile value in the grid at coords x, y
    def setTile(self, x, y, value):
        self.data[y][x] = value

    # Count how many tiles of a given type are present in the grid
    def countTiles(self, tile):
        return sum([row.count(tile) for row in self.data])

    # Function to iterate through tiles adjacent to give x,y coords
    def getAdjacentTiles(self, x, y):
        for yMod in self.adjacentRange:
            for xMod in self.adjacentRange:
                yield self.getTile(x + xMod, y + yMod)

    # Function to simulate a grid for 1 round
    def simulateOnce(self):
        # Create a reference copy because the tiles need to be updated without
        # being influenced by other simulatneous updates.
        reference = self.copy()

        # Iterate through each cell in the grid
        xSize, ySize = self.gridSize()
        for y in range(ySize):
            for x in range(xSize):
                value = reference.getTile(x, y)

                # If tile is empty seat and all surrounding seats are empty,
                # the seat becomes occupied.
                if value is Tile.EmptySeat:
                    occupy = True
                    for tile in reference.getAdjacentTiles(x, y):
                        if tile is Tile.OccupiedSeat:
                            occupy = False
                    if occupy:
                        self.setTile(x, y, Tile.OccupiedSeat)

                # If tile is occupied seat and 4+ surrounding seats are also
                # occupied, the seat will become empty.
                if value is Tile.OccupiedSeat:
                    occupied = -1  # To account for THIS tile
                    for tile in reference.getAdjacentTiles(x, y):
                        if tile is Tile.OccupiedSeat:
                            occupied += 1
                    if occupied >= self.occupiedTolerance:
                        self.setTile(x, y, Tile.EmptySeat)

    # Function to simulate grid until no changes are detected
    def simulateUntilEquilibrium(self):
        state = self.serialize()
        while True:
            self.simulateOnce()
            newState = self.serialize()
            if newState == state:
                break
            state = newState


# Subclass of the SimpleGrid which implements a line-of-sight adjacency
# algorith, and a large occupancy tolerance
class AdvancedGrid(SimpleGrid):
    occupiedTolerance = 5

    # This overridden function uses "line-of-sight" instead of only just
    # checking the 8 adjacent tiles
    def getAdjacentTiles(self, x, y):
        for yMod in self.adjacentRange:
            for xMod in self.adjacentRange:
                i = 1
                while True:
                    tile = self.getTile(x + (xMod * i), y + (yMod * i))
                    i += 1

                    if tile is Tile.Floor:
                        continue

                    yield tile
                    break


# Parse the input lines into a map grid, replacing characters with enums
inputGridData = []
for line in inputLines:
    line = line.strip()
    if not line:
        continue
    inputGridData.append([Tile(c) for c in line])

# Print a warning
print(
    f"{Fore.YELLOW}Warning:{Style.RESET_ALL} It may take awhile to compute the answers to parts 1 and 2..."
)

# For part 1, we need to run the simple grid through simulations until it
# reach equilibrium (no longer changes).
gridP1 = SimpleGrid(inputGridData)
gridP1.simulateUntilEquilibrium()
print(
    f"{Fore.GREEN}Answer (P1):{Style.RESET_ALL} {gridP1.countTiles(Tile.OccupiedSeat)}"
)

# For part 2, we need to do the same thing, but using the advanced grid
# which uses a different line-of-sight algorithm.
gridP2 = AdvancedGrid(inputGridData)
gridP2.simulateUntilEquilibrium()
print(
    f"{Fore.GREEN}Answer (P2):{Style.RESET_ALL} {gridP2.countTiles(Tile.OccupiedSeat)}"
)
