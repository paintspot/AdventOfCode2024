# Advent of Code 2024 day 2
noOfSafe = 0

with open(".\\input.txt", "r") as file:
    for line in file:
        values = list(map(int, line.split()))

        increasing = values[0] < values[1]  # Determine increasing/decreasing order

        result = True  # Assume it's safe unless proven otherwise
        for i in range(len(values) - 1):
            absolute = abs(values[i] - values[i + 1])

            if absolute == 0 or absolute > 3:  # Difference check
                result = False
                break

            if (increasing and values[i] > values[i + 1]) or (not increasing and values[i] < values[i + 1]):
                result = False
                break

        if result:
            noOfSafe += 1

print(noOfSafe)
