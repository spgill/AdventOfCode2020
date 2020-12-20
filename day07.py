# stdlib imports
import re

# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
        inputLines = inputHandle.readlines()

    seeking = "shiny gold"

    # We first have to iterate through all of the input lines and create
    # a mapping to describe what each bag contains
    bags = dict()
    for line in inputLines:
        if not len(line.strip()):
            continue
        bagName, contentsLine = re.match(
            r"^(.*?) bags contain (.*)$", line.strip()
        ).groups()
        contents = re.findall(r"(\d+) (.*?) bags?", contentsLine)
        bags[bagName] = {name: int(count) for count, name in contents}

    # Method to recursively find contents of a bag
    def getBagNamesWithin(name):
        bagNames = set()
        bagNames.add(name)
        contents = bags[name]
        for bagName in contents:
            bagNames = bagNames.union(getBagNamesWithin(bagName))
        return bagNames

    # Answer for part 1 is the number of bag colors that eventually contain
    # a shiny gold bag
    found = sum(
        [
            int(seeking in getBagNamesWithin(bagName))
            for bagName in bags
            if bagName != seeking
        ]
    )
    aoc.printAnswer(1, found)

    # Method to recursively find contents of a bag
    def countBagContents(name):
        count = 1
        contents = bags[name]
        for bagName, bagCount in contents.items():
            count += bagCount * countBagContents(bagName)
        return count

    # Answer for part 2 is the number of bags contained within a single
    # shiny gold bag. We subtract 1 to account for the gold bag itself.
    aoc.printAnswer(2, countBagContents(seeking) - 1)


if __name__ == "__main__":
    main()
