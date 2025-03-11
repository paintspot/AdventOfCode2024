# Advent of Code 2024 day 3
import re

def addMuls(content):
    result = 0
    multipliers = re.findall(r"mul\(\d+\,\d+\)", content)

    for multiplier in multipliers:
        numbers = re.findall(r"\d+", multiplier)
        result += int(numbers[0]) * int(numbers[1])

    return result

result = 0
with open(".\\input.txt", "r") as fileobj:
    content = fileobj.read()
    muls = re.finditer(r"mul\(\d+\,\d+\)", content)
    dos = re.finditer(r"do\(\)", content)
    donts = re.finditer(r"don't\(\)", content)
    
# for multiplier in multipliers:
#     numbers = re.findall("\d+", multiplier)
#     result += int(numbers[0]) * int(numbers[1])
dos_start_list =[]
donts_start_list=[]
for do in dos:
    dos_start_list.append(do.start())

for dont in donts: 
    donts_start_list.append(dont.start())

combined = []
combined.append(donts_start_list.pop(0))

add_dont = False

while (len(donts_start_list) > 0 and len(dos_start_list) > 0):
    if add_dont:
        if donts_start_list[0] > combined[-1]:
            combined.append(donts_start_list.pop(0))
            add_dont = False
        else:
            donts_start_list.pop(0)
    else:
        if dos_start_list[0] > combined[-1]:
            combined.append(dos_start_list.pop(0))
            add_dont = True
        else:
            dos_start_list.pop(0)

if len(dos_start_list) > 0:
    combined.append(dos_start_list.pop(0))
    
result = addMuls(content[:combined[0]])

for i in range(2,len(combined),2):
    result += addMuls(content[combined[i-1]:combined[i]])

if len(combined) % 2 == 0:
     result += addMuls(content[combined[-1]:])

print(result)
