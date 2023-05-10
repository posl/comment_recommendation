def main():
    N = int(input())
    trampolines = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    adj = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            xi, yi, pi = trampolines[i]
            xj, yj, pj = trampolines[j]
            if pi * 1 >= abs(xi - xj) + abs(yi - yj):
                adj[i][j] = True
    for k in range(N):
        for i in range(N):
            for j in range(N):
                adj[i][j] |= adj[i][k] and adj[k][j]
    ans = 1 << 30
    for i in range(N):
        ok = True
        for j in range(N):
            if not adj[i][j]:
                ok = False
                break
        if not ok:
            continue
        cnt = 0
        for j in range(N):
            if adj[j][i]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)
