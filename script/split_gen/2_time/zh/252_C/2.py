def solve():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = 1e9
    for i in range(n):
        t = 0
        for j in range(n):
            cnt = 0
            for k in range(10):
                if s[i][k] == s[j][k]:
                    cnt += 1
            t = max(t, cnt)
        ans = min(ans, t)
    print(ans)
solve()
