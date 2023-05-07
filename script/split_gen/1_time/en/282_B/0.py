def solve():
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ok = True
            for k in range(m):
                if s[i][k] == "o" or s[j][k] == "o":
                    continue
                ok = False
            if ok:
                ans += 1
    print(ans)
