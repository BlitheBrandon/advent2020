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
    """Convert each item to an int and return as new list"""
    return [int(item) for item in seq]


def solution_part_one(inp):
    """Return product of first two integers that add up to 2020"""
    for position, value_a in enumerate(inp[0:-1]):
        if (2020 - value_a) in inp[position+1:]:
            return value_a * (2020 - value_a)


def solution_part_two(inp):
    """Return product of first three integers that add up to 2020"""
    for position, value_a in enumerate(inp[0:-1]):
        for value_b in inp[position+1:]:
            if (2020 - value_a - value_b) in inp[position+1:]:
                return value_a * value_b * (2020 - value_a - value_b)


def main():
    aoc_day = 1
    exercise_input = get_exercise_input_from_file(aoc_day)
    clean_input = clean_data(exercise_input)

    print("Advent of Code part one:", solution_part_one(clean_input))
    print("Advent of Code part two:", solution_part_two(clean_input))


if __name__ == "__main__":
    main()
