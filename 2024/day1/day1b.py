from collections import Counter

#create lists
a, b = [], []

#input into lists
with open("input.txt", "r") as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)

#init ans
ans = 0

#init counter
counter = Counter(b)

#count a value in b
for val in a:
    count = counter.get(val, 0)
    score = val * count
    ans += score

#print ans
print(ans)