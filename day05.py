# stdlib imports
import itertools

# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    # Strip newline characters from the lines
    with path.open("r") as inputHandle:
        inputLines = [line.strip() for line in inputHandle.readlines()]

    # Iterate over each line, each of which is a "boarding pass", and
    # parse the "seat id" for each one.
    seatIds = []
    for line in inputLines:
        seatIds.append(
            int(
                line.replace("F", "0")
                .replace("B", "1")
                .replace("L", "0")
                .replace("R", "1"),
                2,
            )
        )

    # The answer to part 1 is the highest seat ID
    aoc.printAnswer(1, max(seatIds))

    # The answer to part 2 is the ID in the middle of three consecutive ID's
    for idList in itertools.combinations(seatIds, 2):
        sortedList = sorted(idList)
        if sortedList[1] == sortedList[0] + 2:
            middleId = sortedList[0] + 1
            if middleId not in seatIds:
                aoc.printAnswer(2, middleId)


if __name__ == "__main__":
    main()
