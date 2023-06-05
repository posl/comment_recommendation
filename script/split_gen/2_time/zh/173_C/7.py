def count(s):
    count = [0,0,0,0]
    for i in s:
        if i == "AC":
            count[0] += 1
        elif i == "WA":
            count[1] += 1
        elif i == "TLE":
            count[2] += 1
        elif i == "RE":
            count[3] += 1
    return count
n = int(input())
s = []
for i in range(n):
    s.append(input())
count = count(s)
print("AC x",count[0])
print("WA x",count[1])
print("TLE x",count[2])
print("RE x",count[3])
