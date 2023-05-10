def dfs(A, N, M, Q, a, b, c, d, ans):
    if len(A) == N:
        score = 0
        for i in range(Q):
            if A[b[i]-1] - A[a[i]-1] == c[i]:
                score += d[i]
        ans[0] = max(ans[0], score)
        return
    for i in range(A[-1], M+1):
        A.append(i)
        dfs(A, N, M, Q, a, b, c, d, ans)
        A.pop()
N, M, Q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
ans = [0]
for i in range(1, M+1):
    dfs([i], N, M, Q, a, b, c, d, ans)
print(ans[0])

if __name__ == '__main__':
    dfs()