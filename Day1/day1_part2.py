# Advent of Code 2024 day 1

column1 = []
column2 = []

with open(".\input.txt", "r") as file:
    for line in file:
        values = line.split()
        column1.append(int(values[0])) 
        column2.append(int(values[1])) 

column1.sort()
column2.sort()
simScoreTotal = 0
simScoreTemp = 0
idxColTwo = 0

for i in range(len(column1)-1):
    j=i+1
    if column1[i] == column1[j]:
        continue
    while idxColTwo < len(column2) and column1[i] >= column2[idxColTwo]:
        if column1[i] == column2[idxColTwo]:
            simScoreTemp += 1
        idxColTwo += 1
    if idxColTwo == len(column2):
        break
    simScoreTotal = simScoreTotal + simScoreTemp * column1[i]
    simScoreTemp = 0

print(simScoreTotal)
