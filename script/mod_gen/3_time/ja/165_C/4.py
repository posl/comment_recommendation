def dfs(A, N, M, Q, a, b, c, d, ans):
    if len(A) == N:
        tmp = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                tmp += d[i]
        ans = max(ans, tmp)
        return ans
    if len(A) == 0:
        A.append(1)
    else:
        A.append(A[-1])
    while A[-1] <= M:
        ans = dfs(A, N, M, Q, a, b, c, d, ans)
        A[-1] += 1
    A.pop()
    return ans
N, M, Q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(Q):
    tmp = list(map(int, input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
    c.append(tmp[2])
    d.append(tmp[3])
ans = 0
A = []
print(dfs(A, N, M, Q, a, b, c, d, ans))

if __name__ == '__main__':
    dfs()