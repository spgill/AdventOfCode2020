# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
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
        for i in [0, 2]:
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
    aoc.printAnswer(1, adapterCount[0] * adapterCount[2])

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
    aoc.printAnswer(2, memory[deviceJoltage])


if __name__ == "__main__":
    main()
