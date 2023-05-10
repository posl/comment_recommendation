def main():
    N = int(input())
    A = [list(map(int, input())) for _ in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            for k in range(N):
                for l in range(N):
                    if k == 0 and l == 0:
                        continue
                    if (i + k) >= N or (j + l) >= N:
                        continue
                    now = 0
                    x, y = i, j
                    dx, dy = k, l
                    for _ in range(N):
                        now *= 10
                        now += A[x][y]
                        x += dx
                        y += dy
                    ans = max(ans, now)
    print(ans)
