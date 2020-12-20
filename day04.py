# stdlib imports
import re

# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
        inputLines = inputHandle.readlines()

    # Separate out the blank line delimited groups, and parse the key values pairs
    # into dictionaries.
    groups = list()
    group = dict()
    for line in inputLines:
        if line == "\n":
            groups.append(group)
            group = dict()
            continue
        for key, value in re.findall(r"(\w+)\:(\S+)", line):
            group[key] = value
    groups.append(group)

    # Iterate through all the groups and count all that have the mandatory fields
    # present (part 1) and have their values within spec (part 2)
    countP1 = 0
    countP2 = 0
    mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for group in groups:
        valid = True
        for name in mandatory:
            if name not in group:
                valid = False

        if not valid:
            continue
        countP1 += 1

        # Birth year
        byr = int(group.get("byr", 0))
        if not 1920 <= byr <= 2002:
            continue

        # Issue year
        iyr = int(group.get("iyr", 0))
        if not 2010 <= iyr <= 2020:
            continue

        # Expiration year
        eyr = int(group.get("eyr", 0))
        if not 2020 <= eyr <= 2030:
            continue

        # Height
        hgt = re.match(r"(\d+)(cm|in)", group.get("hgt", "0in"))
        if hgt is None:
            continue
        hgtValue, hgtUnit = hgt.groups()
        hgtValue = int(hgtValue)
        if hgtUnit not in ["cm", "in"]:
            continue
        elif hgtUnit == "cm" and not 150 <= hgtValue <= 193:
            continue
        elif hgtUnit == "in" and not 59 <= hgtValue <= 76:
            continue

        # Hair color
        hcl = group.get("hcl", "")
        if re.match(r"#[0-9a-f]{6}", hcl) is None:
            continue

        # Eye color
        ecl = group.get("ecl", "")
        if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            continue

        # Passport ID
        pid = group.get("pid", "")
        if re.match(r"^\d{9}$", pid) is None:
            continue

        countP2 += 1

    aoc.printAnswer(1, countP1)
    aoc.printAnswer(2, countP2)


if __name__ == "__main__":
    main()
