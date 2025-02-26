# Advent of Code 2024 day 1

column1 = []
column2 = []

with open("input.txt", "r") as file:
    for line in file:
        values = line.split()
        column1.append(int(values[0])) 
        column2.append(int(values[1])) 

column1.sort()
column2.sort()
distance = 0

for i in range(len(column1)):
    if column1[i] >= column2[i]:
        distance += column1[i] - column2[i]
    else:
        distance += column2[i] - column1[i]

print(distance)
