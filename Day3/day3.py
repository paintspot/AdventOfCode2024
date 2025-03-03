# Advent of Code 2024 day 3
import re
result = 0
with open(".\\input.txt", "r") as fileobj:
    content = fileobj.read()
    multipliers = re.findall(r"mul\(\d+\,\d+\)", content)

for multiplier in multipliers:
    numbers = re.findall("\d+", multiplier)
    result += int(numbers[0]) * int(numbers[1])

print(result)