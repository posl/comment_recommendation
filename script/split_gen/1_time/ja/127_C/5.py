def main():
    N, M = map(int, input().split())
    l = [0] * (N + 1)
    r = [0] * (N + 1)
    for _ in range(M):
        L, R = map(int, input().split())
        l[L] += 1
        r[R] += 1
    ans = 0
    now = 0
    for i in range(1, N + 1):
        now += l[i]
        if now == M:
            ans += 1
        now -= r[i]
    print(ans)
