def dfs(A, N, M, Q, a, b, c, d, ans):
    if len(A) == N:
        tmp = 0
        for i in range(Q):
            if A[b[i]-1] - A[a[i]-1] == c[i]:
                tmp += d[i]
        ans[0] = max(ans[0], tmp)
        return
    A.append(A[-1])
    while A[-1] <= M:
        dfs(A, N, M, Q, a, b, c, d, ans)
        A[-1] += 1
    A.pop()
N, M, Q = map(int, input().split())
a, b, c, d = [], [], [], []
for i in range(Q):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)
ans = [0]
A = [1]
dfs(A, N, M, Q, a, b, c, d, ans)
print(ans[0])

if __name__ == '__main__':
    dfs()