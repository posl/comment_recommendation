def dfs(v, color):
    global N
    global M
    global A
    global B
    global ans
    global used
    if v == N:
        ans += 1
        return
    for i in range(3):
        if color == i:
            continue
        for j in range(M):
            if A[j] == v + 1:
                used[B[j] - 1] = True
            if B[j] == v + 1:
                used[A[j] - 1] = True
        for k in range(N):
            if used[k]:
                continue
            dfs(v + 1, k)
        for j in range(M):
            if A[j] == v + 1:
                used[B[j] - 1] = False
            if B[j] == v + 1:
                used[A[j] - 1] = False
N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
ans = 0
used = [False] * N
dfs(0, 0)
print(ans)

if __name__ == '__main__':
    dfs()