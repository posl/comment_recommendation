def dfs(a):
    if len(a) == N:
        score = 0
        for i in range(Q):
            if a[b[i]-1] - a[a[i]-1] == c[i]:
                score += d[i]
        return score
    else:
        a.append(a[-1])
        while a[-1] <= M:
            dfs(a)
            a[-1] += 1
        a.pop()
N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
print(dfs([1]))
