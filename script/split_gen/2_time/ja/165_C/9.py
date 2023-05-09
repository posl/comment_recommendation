def dfs(a, b, c, d, n, m, q, A, ans):
    if len(A) == n:
        if ans[0] < sum(d[i] for i in range(q) if A[b[i] - 1] - A[a[i] - 1] == c[i]):
            ans[0] = sum(d[i] for i in range(q) if A[b[i] - 1] - A[a[i] - 1] == c[i])
    else:
        for v in range(a[len(A) - 1], m + 1):
            A.append(v)
            dfs(a, b, c, d, n, m, q, A, ans)
            A.pop()
n, m, q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(q):
    a_, b_, c_, d_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)
    d.append(d_)
ans = [0]
for v in range(1, m + 1):
    dfs(a, b, c, d, n, m, q, [v], ans)
print(ans[0])
