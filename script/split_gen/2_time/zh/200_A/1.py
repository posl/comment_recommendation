def dfs(i, color):
    global N, M, A, B, ans
    if i == N:
        ans += 1
        return
    for c in range(3):
        color[i] = c
        ok = True
        for j in range(M):
            if A[j] == i+1 and color[B[j]-1] == c:
                ok = False
                break
            if B[j] == i+1 and color[A[j]-1] == c:
                ok = False
                break
        if ok:
            dfs(i+1, color)
N, M = map(int, input().split())
A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
color = [0]*N
ans = 0
dfs(0, color)
print(ans)
