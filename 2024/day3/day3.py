import re

#init list
valid = []
ans = 0

#open file
with open("input.txt", "r") as f:
    input = f.read()

    #check for regex
    valid = re.findall("mul\((\d{1,4}),(\d{1,4})\)", input)

for tuple in valid:
    ans += int(tuple[0]) * int(tuple[1])

print(ans)