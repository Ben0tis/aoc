#create lists
a, b = [], []

#input into lists
with open("input.txt", "r") as f:
    for line in f.readlines():
        x, y = (int(z) for z in line.split())
        a.append(x)
        b.append(y)
    
#sort lists
a.sort()
b.sort()

#init ans
ans = 0

#compute difference + add to ans
for la, lb in zip(a, b):
    ans += abs(la - lb)

#print ans
print(ans)