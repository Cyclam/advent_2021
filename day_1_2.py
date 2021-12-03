

with open('measurements.txt', 'r', encoding='utf-8') as measurements:
    measurement_1 = int(measurements.readline())
    measurement_2 = int(measurements.readline())
    measurement_3 = int(measurements.readline())
    previous_average = (measurement_1 + measurement_2 + measurement_3) / 3
    counter = 0
    for measurement in measurements:
        measurement_1 = measurement_2
        measurement_2 = measurement_3
        measurement_3 = int(measurement)
        this_average = (measurement_1 + measurement_2 + measurement_3) / 3
        if this_average > previous_average:
            counter += 1
        previous_average = this_average

print(f"averages that were larger than the previous: {counter}")