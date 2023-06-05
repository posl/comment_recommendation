def solve():
    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for i in range(1, n):
        cnt += i * (n - i)
    for i in range(1, 1 << n):
        for j in range(1, 1 << n):
            if i & j == 0:
                continue
            s = 0
            for a in range(n):
                for b in range(n):
                    if (i >> a) & 1 and (j >> b) & 1:
                        s += t[a][b]
            if s == k:
                cnt -= 1
    print(cnt)
solve()
