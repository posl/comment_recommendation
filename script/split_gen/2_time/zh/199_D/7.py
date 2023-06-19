def main():
    n, m = map(int, input().split())
    g = [[False for i in range(n)] for j in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        g[a-1][b-1] = True
        g[b-1][a-1] = True
    ans = 0
    for i in range(1, 2**n):
        ok = True
        for j in range(n):
            if i>>j&1:
                for k in range(j+1, n):
                    if i>>k&1:
                        if g[j][k]:
                            ok = False
        if ok:
            ans += 1
    print(ans)
