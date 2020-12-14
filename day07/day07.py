from sys import exit


def get_exercise_input_from_file(num):
    """Read aoc input from file and return as list"""
    fname = f"day{num:02}_input.txt"
    try:
        with open(fname, "r") as f:
            return f.read().split("\n")
    except FileNotFoundError:
        exit(f"File {repr(fname)} not found.")


def clean_data(inp):
    """Build bag dictionary from inp,"""
    bag_dict = dict()
    
    for line in inp:
        bag, bag_contents = line.split(" bags contain ")
        bag_dict[bag] = []
        
        if bag_contents != "no other bags.":
            tmp = bag_contents.rstrip(".").rsplit(", ")
            for item in tmp:
                num_bags, bag_name = item.split(" ", 1)
                trimmed_name, _ = bag_name.rsplit(" ", 1)
                bag_dict[bag].append(trimmed_name)
    return bag_dict


def clean_data_part_two(inp):
    """Build bag dictionary from inp,"""
    bag_dict = dict()
    
    for line in inp:
        bag, bag_contents = line.split(" bags contain ")
        bag_dict[bag] = []
        
        if bag_contents != "no other bags.":
            tmp = bag_contents.rstrip(".").rsplit(", ")
            for item in tmp:
                num_bags, bag_name = item.split(" ", 1)
                trimmed_name, _ = bag_name.rsplit(" ", 1)
                bag_dict[bag].extend(int(num_bags) * [trimmed_name])
    return bag_dict


def solution_part_one(bags):
    """"""
    result = set()
    bag_queue = ["shiny gold"]
    while bag_queue:
        bag_name = bag_queue[0]
        for key in bags.keys():
            if bag_name in bags[key]:
                bag_queue.append(key)
        result.add(bag_name)
        bag_queue.pop(0)
    return len(result) - 1


def solution_part_two(bags):
    """Return count of bags within shiny gold bag"""
    bag_count = 0
    bag_queue = ["shiny gold"]
    while bag_queue:
        bag_name = bag_queue[0]
        if bags[bag_name]:
            bag_queue.extend(bags[bag_name])
            bag_count += len(bags[bag_name])
        bag_queue.pop(0)
    return bag_count


def main():
    """Get day's input and pass to day's two functions

    Set day of month, get that day's exercise input from file,
    pass input to part one and part two's functions, print results
    """
    aoc_day = 7
    exercise_input = get_exercise_input_from_file(aoc_day)
    clean_input = clean_data(exercise_input)
    clean_input_part_two = clean_data_part_two(exercise_input)

    print("Advent of Code part one:", solution_part_one(clean_input))
    print("Advent of Code part two:", solution_part_two(clean_input_part_two))


if __name__ == "__main__":
    main()
