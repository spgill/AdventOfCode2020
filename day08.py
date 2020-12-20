# stdlib imports
import copy

# vendor imports
import spgill.util.aoc as aoc


@aoc.solution
def main(path):
    with path.open("r") as inputHandle:
        inputLines = inputHandle.readlines()

    # Iterate through the input and parse the lines into instructions
    inputInstructions = list()
    for line in inputLines:
        line = line.strip()
        if not len(line):
            continue
        op, arg = line.split(" ")
        inputInstructions.append([op, int(arg)])

    # Function to execute instructions list
    def execute(instructions):
        position = 0
        accumulator = 0
        completed = True
        executed = set()
        while True:
            # If the program reaches the end, break and return
            if position == len(instructions):
                break

            # If the program reaches a previously execute instruction, abort
            if position in executed:
                completed = False
                break

            executed.add(position)

            op, arg = instructions[position]

            # Accumulator operator
            if op == "acc":
                accumulator += arg

            # Jump operator
            if op == "jmp":
                position += arg

            else:
                position += 1

        return (completed, accumulator)

    # Answer to part 1 is the value of the accumulator at the end of the 1st loop
    aoc.printAnswer(1, execute(inputInstructions)[1])

    # Next, we need to try executing different permutations of the instruction
    # set until we find one that completes successfully.
    for i, inspect in enumerate(inputInstructions):
        if inspect[0] not in ["nop", "jmp"]:
            continue

        # Make a copy of the inspected instruction, and reverse the operation
        replacementInstruction = copy.copy(inspect)
        if replacementInstruction[0] == "nop":
            replacementInstruction[0] = "jmp"
        else:
            replacementInstruction[0] = "nop"

        # Temporarily replace the inspected instruction
        inputInstructions[i] = replacementInstruction

        # If the execution completes successfully, the accumulator value
        # is the answer to part 2
        completed, accumulator = execute(inputInstructions)
        if completed:
            aoc.printAnswer(2, accumulator)
            break

        # Else, replace the original instruction in the list
        else:
            inputInstructions[i] = inspect


if __name__ == "__main__":
    main()
