def dfs(i, sum):
    global N
    global S
    global a
    global b
    global ans
    if i == N:
        if sum == S:
            ans = True
        return
    dfs(i+1, sum+a[i])
    dfs(i+1, sum+b[i])
N, S = map(int, input().split())
a = []
b = []
for i in range(N):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
ans = False
dfs(0, 0)
