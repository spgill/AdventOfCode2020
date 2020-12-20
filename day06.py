# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
        inputGroups = inputHandle.read().split("\n\n")

    abet = set("abcdefghijklmnopqrstuvwxyz")

    # Iterate through the groups and the unique number of letters for each
    # person in each group. Part 1 is finding the unique answers for anyone
    # in a group (union). Part 2 is finding the unique answers that
    # everyone gave (intersection).
    totalP1, totalP2 = 0, 0
    for group in inputGroups:
        anyone = set()
        everyone = abet

        for line in group.strip().split("\n"):
            unique = set()
            for char in line:
                if char in abet:
                    unique.add(char)
            anyone = anyone.union(unique)
            everyone = everyone.intersection(unique)

        totalP1 += len(anyone)
        totalP2 += len(everyone)

    aoc.printAnswer(1, totalP1)
    aoc.printAnswer(2, totalP2)


if __name__ == "__main__":
    main()
