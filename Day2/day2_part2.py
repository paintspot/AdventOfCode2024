# Advent of Code 2024 day 2


def safeChecker(values):
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
            return True
        return False

with open(".\\input.txt", "r") as file:
    noOfSafe = 0
    for line in file:
        values = list(map(int, line.split()))
        if safeChecker(values):
             noOfSafe += 1
        else:
            for i in range(len(values)):
                tmp = values[:i] + values[i+1:]
                if safeChecker(tmp):
                    noOfSafe += 1
                    break 
print(noOfSafe)