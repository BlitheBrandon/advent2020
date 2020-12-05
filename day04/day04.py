from sys import exit


def get_exercise_input_from_file(num):
    """Read aoc input from file and return as list"""
    fname = f"day{num:02}_input.txt"
    try:
        with open(fname, "r") as f:
            return f.readlines()
    except FileNotFoundError:
        exit(f"File {repr(fname)} not found.")


def clean_data(seq):
    """Join strings into single passport entry"""
    entries = []
    tmp = []

    for line_num, line_content in enumerate(seq):
        if line_content == "\n":
            if tmp:
                entries.append("".join(tmp))
                tmp = []
        else:
            tmp.append(line_content.replace("\n", " "))
    if tmp:
        entries.append("".join(tmp))

    return entries


def solution_part_one(inp):
    """Return count of valid passport entries"""
    # This is a hack.
    # I'm counting colons in the entry, not the validity of field names

    passport_count = 0
    for entry in inp:
        num_fields = entry.count(":")
        if num_fields == 8 or (num_fields == 7 and "cid" not in entry):
            passport_count += 1
    return passport_count


def valid_passport(passport_dict):
    """Verify passport has enough fields and that they contain valid data"""
    # Used for AOC part two

    valid_field_count = 0

    if 1920 <= int(passport_dict.get("byr", 0)) <= 2002:
        valid_field_count += 1

    if 2010 <= int(passport_dict.get("iyr", 0)) <= 2020:
        valid_field_count += 1

    if 2020 <= int(passport_dict.get("eyr", 0)) <= 2030:
        valid_field_count += 1

    if len(passport_dict.get("hgt", "")) >= 4:
        val = int(passport_dict["hgt"][0:-2])
        unit = passport_dict["hgt"][-2:]
        if unit == "cm" and 150 <= val <= 193:
            valid_field_count += 1
        if unit == "in" and 59 <= val <= 76:
            valid_field_count += 1

    hcl_id = passport_dict.get("hcl", "")
    if hcl_id and hcl_id[0] == "#" and hcl_id[1:].isalnum():
        valid_field_count += 1

    eye_colors = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    if passport_dict.get("ecl", "") in eye_colors:
        valid_field_count += 1

    if passport_dict.get("pid", "").isdigit() and len(passport_dict.get("pid", "")) == 9:
        valid_field_count += 1

    if valid_field_count >= 7:
        return True
    return False


def solution_part_two(inp):
    """Count how many passport entries are valid"""
    passport_count = 0
    passport_dict = dict()
    for entry in inp:
        fields = entry.split(" ")
        for field in fields:
            if field:
                k, v = field.split(":")
                passport_dict[k] = v

        if valid_passport(passport_dict):
            passport_count += 1
        passport_dict.clear()

    return passport_count


def main():
    """Get day's input and pass to day's two functions

    Set day of month, get that day's exercise input from file,
    pass input to part one and part two's functions, print results
    """
    aoc_day = 4
    exercise_input = get_exercise_input_from_file(aoc_day)
    clean_input = clean_data(exercise_input)

    print("Advent of Code part one:", solution_part_one(clean_input))
    print("Advent of Code part two:", solution_part_two(clean_input))


if __name__ == "__main__":
    main()
