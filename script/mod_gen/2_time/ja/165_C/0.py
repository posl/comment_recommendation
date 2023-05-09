def dfs(A):
    global ans
    if len(A) == N:
        score = 0
        for i in range(Q):
            if A[b[i]-1] - A[a[i]-1] == c[i]:
                score += d[i]
        ans = max(ans, score)
        return
    for i in range(A[-1], M+1):
        dfs(A+[i])
N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for _ in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
ans = 0
for i in range(1, M+1):
    dfs([i])
print(ans)

if __name__ == '__main__':
    dfs()