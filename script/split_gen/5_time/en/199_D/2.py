def main():
    n, m = map(int, input().split())
    g = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a - 1][b - 1] = True
        g[b - 1][a - 1] = True
    ans = 0
    for i in range(1 << n):
        ok = True
        for j in range(n):
            for k in range(j + 1, n):
                if (i & (1 << j)) and (i & (1 << k)) and g[j][k]:
                    ok = False
        if ok:
            ans += 1
    print(ans)
