from sys import exit


def get_exercise_input_from_file(num):
    """Read aoc input from file and return as list"""
    fname = f"day{num:02}_input.txt"
    try:
        with open(fname, "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        exit(f"File {repr(fname)} not found.")


def solution_part_one(inp, row_offset=1, col_offset=3):
    """Return count of trees (#) seen along a given path (row, col offsets)"""
    tree_count = 0
    row_num = 0
    col_num = 0
    width = len(inp[0])
    while True:
        row_num += row_offset
        col_num = (col_num + col_offset) % width
        if inp[row_num][col_num] == "#":
            tree_count += 1
        if row_num + row_offset > len(inp) - 1:
            break
    return tree_count


def solution_part_two(inp, offsets):
    """Return product of trees seen for multiple paths"""
    total = 1
    for r, c in offsets:
        tree_count = solution_part_one(inp, r, c)
        if tree_count:
            total *= tree_count
    return total


def main():
    """Get day's input and pass to day's two functions

    Set day of month, get that day's exercise input from file,
    pass input to part one and part two's functions, print results
    """

    aoc_day = 3
    exercise_input = get_exercise_input_from_file(aoc_day)
    part_two_offsets = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))

    print("Advent of Code part one:", solution_part_one(exercise_input))
    print("Advent of Code part two:",
          solution_part_two(exercise_input, part_two_offsets))


if __name__ == "__main__":
    main()
