def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input())))
    ans = -1
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if i == n - 1 and j == n - 1:
                continue
            num = a[i][j]
            x = 0
            y = 0
            for k in range(n - 1):
                if x == 0 and y == 0:
                    if i + 1 < n:
                        x = i + 1
                        y = j
                    else:
                        x = i
                        y = j + 1
                elif x == n - 1 and y == n - 1:
                    if i > 0:
                        x = i - 1
                        y = j
                    else:
                        x = i
                        y = j - 1
                elif x == 0:
                    if y + 1 < n:
                        x = i
                        y = j + 1
                    else:
                        x = i + 1
                        y = j
                elif x == n - 1:
                    if y > 0:
                        x = i
                        y = j - 1
                    else:
                        x = i - 1
                        y = j
                elif y == 0:
                    if x > 0:
                        x = i - 1
                        y = j
                    else:
                        x = i
                        y = j + 1
                elif y == n - 1:
                    if x + 1 < n:
                        x = i + 1
                        y = j
                    else:
                        x = i
                        y = j - 1
                elif x + 1 < n and y + 1 < n:
                    x = x + 1
                    y = y + 1
                elif x > 0 and y > 0:
                    x = x - 1
                    y = y - 1
                num = num * 10 + a[x][y]
            if ans < num:
                ans = num
    print(ans)

if __name__ == '__main__':
    main()