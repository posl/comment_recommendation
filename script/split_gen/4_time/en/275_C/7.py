def check(s):
    if s[0] == "#" and s[1] == "#" and s[4] == "#" and s[5] == "#":
        return True
    else:
        return False
s = []
for i in range(9):
    s.append(input())
count = 0
for i in range(9):
    if i == 0 or i == 1 or i == 3 or i == 4 or i == 6 or i == 7:
        if check(s[i]):
            count += 1
    else:
        if s[i][3] == "#" and s[i][4] == "#" and s[i][7] == "#" and s[i][8] == "#":
            count += 1
print(count)
