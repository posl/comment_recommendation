def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        s[i] = list(s[i])
    for i in range(n):
        for j in range(n):
            if s[i][j] == '#':
                s[i][j] = 1
            else:
                s[i][j] = 0
    for i in range(n):
        for j in range(n):
            if i >= 1:
                s[i][j] += s[i - 1][j]
            if j >= 1:
                s[i][j] += s[i][j - 1]
            if i >= 1 and j >= 1:
                s[i][j] -= s[i - 1][j - 1]
    def calc(x1, y1, x2, y2):
        res = s[x2][y2]
        if x1 >= 1:
            res -= s[x1 - 1][y2]
        if y1 >= 1:
            res -= s[x2][y1 - 1]
        if x1 >= 1 and y1 >= 1:
            res += s[x1 - 1][y1 - 1]
        return res
    for i in range(n):
        for j in range(n):
            if s[i][j] == 0:
                if calc(i, j, i + 1, j + 1) == 0:
                    print('Yes')
                    exit()
                if i + 2 <= n and j + 2 <= n and calc(i, j, i + 2, j + 2) == 2:
                    print('Yes')
                    exit()
                if i + 3 <= n and j + 3 <= n and calc(i, j, i + 3, j + 3) == 3:
                    print('Yes')
                    exit()
                if i + 4 <= n and j + 4 <= n and calc(i, j, i + 4, j + 4) == 4:
                    print('Yes')
                    exit()
                if i + 5 <= n and j + 5 <= n and calc(i, j, i + 5, j + 5) == 5:
                    print('Yes')
                    exit()
                if

if __name__ == '__main__':
    main()