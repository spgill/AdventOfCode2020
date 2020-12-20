# stdlib imports
import functools

# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
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
            aoc.printAnswer(1, trees)

    # The answer for part 2 is the product of all slope counts
    product = functools.reduce(lambda a, b: a * b, counts)
    aoc.printAnswer(2, product)


if __name__ == "__main__":
    main()
