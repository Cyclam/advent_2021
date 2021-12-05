

with open("day_3_power.txt", "r", encoding="utf-8") as power:
    column_totals = []

    # first line, set up our variables:
    line = power.readline()
    for index, bit in enumerate(line.strip()):
        column_totals.insert(index, int(bit))

    total_lines = 1
    # Now iterate over all other lines
    for line in power:
        total_lines += 1
        for index, bit in enumerate(line.strip()):
            column_totals[index] += int(bit)

    print(f"column_totals: {column_totals}")
    gamma_binary = ""
    epsilon_binary = ""
    for index, column in enumerate(column_totals):
        if column > (total_lines / 2):
            gamma_binary += "1"
            epsilon_binary += "0"
        else:
            gamma_binary += "0"
            epsilon_binary += "1"

    gamma = int(gamma_binary,2 )
    epsilon = int(epsilon_binary, 2)

    print(f"total_lines: {total_lines}")
    print(f"gamma_binary ({gamma_binary}) = {gamma}")
    print(f"epsilon_binary ({epsilon_binary}) = {epsilon}")
    print(f"total power: {gamma * epsilon}")