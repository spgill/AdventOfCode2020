# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
        inputLines = inputHandle.readlines()

    # Parse the input lines into numbers
    values = [int(s.strip()) for s in inputLines if s.strip()]

    # Iterate through every line (after 25) and check if the number is the
    # sum of two of the previous 25 numbers
    invalid = 0
    preamble = i = 25
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
    aoc.printAnswer(1, invalid)

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
    aoc.printAnswer(2, correctSet[0] + correctSet[-1])


if __name__ == "__main__":
    main()
