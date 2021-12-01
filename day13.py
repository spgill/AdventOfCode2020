# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
        inputLines = inputHandle.readlines()

    # Parse the input lines and convert to ints
    earliest = int(inputLines[0].strip())
    services = [
        int(n) if n != "x" else n for n in inputLines[1].strip().split(",")
    ]

    # For part 1, we iterate through departure times looking for the bus
    # that can depart earliest
    current = earliest
    found = 0
    while not found:
        for service in services:
            if service == "x":
                continue
            if current % service == 0:
                found = service
                break
        else:
            current += 1

    # The answer to part 1 is the product of the bus ID and the number of
    # minutes needed to wait.
    aoc.printAnswer(1, found * (current - earliest))

    # For part 2, we need to find a timestamp where bus schedules line up
    # perfectly in succession (skipping 'x' slots)
    timestamp, step = 0, 1
    for offset, service in enumerate(services):
        if service == "x":
            continue
        while (timestamp + offset) % service:
            timestamp += step
        step *= service
    aoc.printAnswer(2, timestamp)


if __name__ == "__main__":
    main()
