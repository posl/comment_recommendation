def is_ok(x, y):
    if x + 5 < n and y + 5 < n:
        if s[x][y] == s[x + 1][y + 1] == s[x + 2][y + 2] == s[x + 3][y + 3] == s[x + 4][y + 4] == s[x + 5][y + 5] == "#":
            return True
    if x + 5 < n and y - 5 >= 0:
        if s[x][y] == s[x + 1][y - 1] == s[x + 2][y - 2] == s[x + 3][y - 3] == s[x + 4][y - 4] == s[x + 5][y - 5] == "#":
            return True
    if x + 5 < n:
        if s[x][y] == s[x + 1][y] == s[x + 2][y] == s[x + 3][y] == s[x + 4][y] == s[x + 5][y] == "#":
            return True
    if y + 5 < n:
        if s[x][y] == s[x][y + 1] == s[x][y + 2] == s[x][y + 3] == s[x][y + 4] == s[x][y + 5] == "#":
            return True
    return False
n = int(input())
s = [input() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == "." and is_ok(i, j):
            print("Yes")
            exit()
print("No")
