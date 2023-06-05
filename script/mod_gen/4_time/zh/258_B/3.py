def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = -1
    for i in range(n):
        for j in range(n):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    x, y = i, j
                    num = a[x][y]
                    for _ in range(n - 1):
                        x += di
                        y += dj
                        if not (0 <= x < n and 0 <= y < n):
                            break
                        num = num * 10 + a[x][y]
                    ans = max(ans, num)
    print(ans)

if __name__ == '__main__':
    main()