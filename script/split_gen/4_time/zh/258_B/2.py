def main():
    n = int(input())
    a = [list(map(int, input())) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    if di == 0 and dj == 0:
                        continue
                    x, y = i, j
                    num = 0
                    while True:
                        num *= 10
                        num += a[x][y]
                        x += di
                        y += dj
                        if x < 0 or x >= n or y < 0 or y >= n:
                            break
                    ans = max(ans, num)
    print(ans)
