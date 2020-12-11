from sys import exit


def get_exercise_input_from_file(num):
    """Read aoc input from file and return as list"""
    fname = f"day{num:02}_input.txt"

    try:
        with open(fname, "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        exit(f"File {repr(fname)} not found.")


def solution_part_one(inp):
    """Convert input to binary, return seats and highest seat"""
    highest_seat = float("-inf")
    seats = []

    for line in inp:
        seq = list(line)
        for i, c in enumerate(seq):
            if c in "FL":
                seq[i] = "0"
            else:
                seq[i] = "1"
        seq = "".join(seq)
        row, col = int(seq[:-3], base=2), int(seq[-3:], base=2)
        seat_num = row * 8 + col
        seats.append(seat_num)
        if seat_num > highest_seat:
            highest_seat = seat_num
    return highest_seat, seats


def solution_part_two(inp):
    """Find empty seat"""
    seats = sorted(inp)
    last_seen = seats[0]
    for n in seats[1:]:
        if n > last_seen + 1:
            return n - 1
        last_seen = n


def main():
    """Get day's input and pass to day's two functions

    Set day of month, get that day's exercise input from file,
    pass input to part one and part two's functions, print results
    """
    aoc_day = 5
    exercise_input = get_exercise_input_from_file(aoc_day)
    part_one, part_two = solution_part_one(exercise_input)
    print("Advent of Code part one:", part_one)
    print("Advent of Code part two:", solution_part_two(part_two))


if __name__ == "__main__":
    main()
