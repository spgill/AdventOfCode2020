# stdlib imports
import itertools

# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
        inputLines = inputHandle.readlines()

    # Part 1, Combine all of the input lines until you find one that sums to 2020
    for a, b in itertools.combinations(inputLines, 2):
        a = int(a)
        b = int(b)
        if a + b == 2020:
            aoc.printAnswer(1, a * b)

    # Part 2, the same thing but with three entries
    for a, b, c in itertools.combinations(inputLines, 3):
        a = int(a)
        b = int(b)
        c = int(c)
        if (a + b + c) == 2020:
            aoc.printAnswer(2, a * b * c)


if __name__ == "__main__":
    main()
