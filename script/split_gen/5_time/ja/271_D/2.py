def dfs(i, s):
    global N, S, A, B, res
    if i == N:
        if s == S:
            res = True
        return
    dfs(i+1, s+A[i])
    dfs(i+1, s+B[i])
N, S = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
res = False
dfs(0, 0)
print('Yes' if res else 'No')
