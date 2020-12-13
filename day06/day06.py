from sys import exit


def get_exercise_input_from_file(num):
    """Read aoc input from file and return as list"""
    fname = f"day{num:02}_input.txt"
    try:
        with open(fname, "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        exit(f"File {repr(fname)} not found.")


def clean_data(seq):
    """Join strings into single passport entry"""
    entries = []
    tmp = []

    for line_content in seq:
        if line_content == "":
            if tmp:
                entries.append("".join(tmp))
                tmp = []
        else:
            tmp.append(line_content.replace("\n", " "))
    if tmp:
        entries.append("".join(tmp))

    return entries


def solution_part_one(inp):
    """Count unique yeses"""
    count = 0
    inp = clean_data(inp)
    for item in inp:
        count += len(set(list(item)))
    return count


def solution_part_two(inp):
    """Count chars contained in everyone's yeses"""
    groups = process_input(inp)
    count = 0
    for yes_answers in groups:
        result = set(yes_answers[0])
        for s in yes_answers[1:]:
            result.intersection_update(s)
        count += len(result)
    return count


def process_input(inp):
    """Split inp into list of lists, seperator is blank line"""
    groups = []
    tmp = []

    for line in inp:
        if not line:
            groups.append(tmp)
            tmp = []
        else:
            tmp.append(line)
    return groups            


def main():
    """Get day's input and pass to day's two functions

    Set day of month, get that day's exercise input from file,
    pass input to part one and part two's functions, print results
    """
    aoc_day = 6
    exercise_input = get_exercise_input_from_file(aoc_day)
    print("Advent of Code part one:", solution_part_one(exercise_input))
    print("Advent of Code part two:", solution_part_two(exercise_input))


if __name__ == "__main__":
    main()
