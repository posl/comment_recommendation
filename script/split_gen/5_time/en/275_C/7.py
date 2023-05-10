def check(r, c):
    if s[r][c] == '#':
        return True
    else:
        return False
s = []
for _ in range(9):
    s.append(input())
ans = 0
for i in range(9):
    for j in range(9):
        if i == 0 or i == 8:
            if j == 0 or j == 8:
                if check(i, j):
                    ans += 1
            else:
                if check(i, j) and check(i, j+1):
                    ans += 1
        else:
            if j == 0 or j == 8:
                if check(i, j) and check(i+1, j):
                    ans += 1
            else:
                if check(i, j) and check(i, j+1) and check(i+1, j) and check(i+1, j+1):
                    ans += 1
print(ans)
