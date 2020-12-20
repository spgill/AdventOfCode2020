# stdlib imports
import re

# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
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

    aoc.printAnswer(1, validP1)

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

    aoc.printAnswer(2, validP2)


if __name__ == "__main__":
    main()
