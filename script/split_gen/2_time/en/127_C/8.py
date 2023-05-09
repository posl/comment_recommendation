def main():
    N, M = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    l = [0] * N
    r = [0] * N
    for i in range(M):
        l[LR[i][0] - 1] += 1
        r[LR[i][1] - 1] += 1
    ans = 0
    now = 0
    for i in range(N):
        now += l[i]
        now -= r[i]
        if now == M:
            ans += 1
    print(ans)
