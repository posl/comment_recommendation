def check(n, names):
    for i in range(n):
        for j in range(n):
            if i != j and (names[i][0] == names[j][0] or names[i][0] == names[j][1] or names[i][1] == names[j][0] or names[i][1] == names[j][1]):
                return False
    return True
n = int(input())
names = []
for i in range(n):
    names.append(input().split())
