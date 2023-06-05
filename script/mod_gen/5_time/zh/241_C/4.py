def check(n, s):
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i][j] = 1
            else:
                s[i][j] = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] == 1:
                if i + 5 < n:
                    if s[i + 1][j] == 1 and s[i + 2][j] == 1 and s[i + 3][j] == 1 and s[i + 4][j] == 1 and s[i + 5][j] == 1:
                        return True
                if j + 5 < n:
                    if s[i][j + 1] == 1 and s[i][j + 2] == 1 and s[i][j + 3] == 1 and s[i][j + 4] == 1 and s[i][j + 5] == 1:
                        return True
                if i + 5 < n and j + 5 < n:
                    if s[i + 1][j + 1] == 1 and s[i + 2][j + 2] == 1 and s[i + 3][j + 3] == 1 and s[i + 4][j + 4] == 1 and s[i + 5][j + 5] == 1:
                        return True
                if i + 5 < n and j - 5 >= 0:
                    if s[i + 1][j - 1] == 1 and s[i + 2][j - 2] == 1 and s[i + 3][j - 3] == 1 and s[i + 4][j - 4] == 1 and s[i + 5][j - 5] == 1:
                        return True
    return False
n = int(input())
s = []
for i in range(n):
    s.append(list(input()))

if __name__ == '__main__':
    check()