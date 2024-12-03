import re

#init list
valid = []
ans = 0

#bool to check for disabled
active = True

#open file
with open("input.txt", "r") as f:
    input = f.read()

    #changed regex to find do and don't
    regex = r"(don't|do)|mul\((\d{1,4}),(\d{1,4})\)"

    #find matches
    matches = re.findall(regex, input)

    #process matches in order found
    for match in matches:
        if match[0] == "don't":
            active = False #disable next muls
        elif match[0] == "do":
            active = True #enable next muls
        elif match[1] and active: #if mul + active
            valid.append((match[1], match[2]))

for tuple in valid:
    ans += int(tuple[0]) * int(tuple[1])

print(ans)