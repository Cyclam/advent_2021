

with open('day_2_course.txt', 'r', encoding='utf-8') as course:
    horizontal = 0
    depth = 0
    aim = 0
    for command in course:
        split_command = command.split()
        if split_command[0] == "forward":
            horizontal += int(split_command[1])
            depth += aim * int(split_command[1])
        elif split_command[0] == "up":
            aim += -int(split_command[1])
        elif split_command[0] == "down":
            aim += int(split_command[1])

print(f"horizontal: {horizontal}\n"
      f"depth: {depth}\n"
      f"sum: {horizontal * depth}")

