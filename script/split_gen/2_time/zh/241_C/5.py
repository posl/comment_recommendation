def check(i, j):
    global s
    if i < 0 or i >= n or j < 0 or j >= n:
        return False
    if s[i][j] == '#':
        return True
    else:
        return False
n = int(input())
s = []
for i in range(n):
    s.append(input())
for i in range(n):
    for j in range(n):
        if check(i, j) and check(i + 1, j) and check(i + 2, j) and check(i + 3, j) and check(i + 4, j) and check(i + 5, j):
            print("Yes")
            exit()
        if check(i, j) and check(i, j + 1) and check(i, j + 2) and check(i, j + 3) and check(i, j + 4) and check(i, j + 5):
            print("Yes")
            exit()
        if check(i, j) and check(i + 1, j + 1) and check(i + 2, j + 2) and check(i + 3, j + 3) and check(i + 4, j + 4) and check(i + 5, j + 5):
            print("Yes")
            exit()
        if check(i, j) and check(i + 1, j - 1) and check(i + 2, j - 2) and check(i + 3, j - 3) and check(i + 4, j - 4) and check(i + 5, j - 5):
            print("Yes")
            exit()
print("No")
