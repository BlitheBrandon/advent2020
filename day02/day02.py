from sys import exit


def get_exercise_input_from_file(num):
    """Read aoc input from file and return as list"""
    fname = f"day{num:02}_input.txt"
    try:
        with open(fname, "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        exit(f"File {repr(fname)} not found.")


def solution_part_one(password_lst):
    """Return count of valid passwords, based on input entry parameters"""
    num_correct_passwords = 0
    for entry in password_lst:
        tmp = entry.split()
        min_count, max_count = map(int, tmp[0].split("-"))
        letter = tmp[1][0]
        password = tmp[2]

        if min_count <= password.count(letter) <= max_count:
            num_correct_passwords += 1
    return num_correct_passwords


def solution_part_two(password_lst):
    """Return count of valid passwords, based on input entry parameters"""
    num_correct_passwords = 0
    for entry in password_lst:
        tmp = entry.split()
        min_count, max_count = map(int, tmp[0].split("-"))
        letter = tmp[1][0]
        password = tmp[2]

        if (password[min_count - 1] == letter) ^ (password[max_count - 1] == letter):
            num_correct_passwords += 1

    return num_correct_passwords


def main():
    """Get day's input and pass to day's two functions

    Set day of month, get that day's exercise input from file,
    pass input to part one and part two's functions, print results
    """
    aoc_day = 2
    exercise_input = get_exercise_input_from_file(aoc_day)

    print("Advent of Code part one:", solution_part_one(exercise_input))
    print("Advent of Code part two:", solution_part_two(exercise_input))


if __name__ == "__main__":
    main()
