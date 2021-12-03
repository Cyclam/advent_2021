

with open('measurements.txt', 'r', encoding='utf-8') as measurements:
    previous_line = int(measurements.readline()) # this should advance the pointer one line
    counter = 0
    for this_line in measurements:
        if int(this_line) > previous_line:
            counter += 1
        previous_line = int(this_line)

print(f"measurements that were larger than the previous: {counter}")