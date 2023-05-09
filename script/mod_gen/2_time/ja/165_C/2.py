def dfs(A):
    global ans
    if len(A) == N:
        tmp = 0
        for a, b, c, d in Q:
            if A[b-1] - A[a-1] == c:
                tmp += d
        ans = max(ans, tmp)
        return
    for i in range(A[-1], M+1):
        dfs(A+[i])
N, M, Q = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(Q)]
ans = 0
for i in range(1, M+1):
    dfs([i])
print(ans)

if __name__ == '__main__':
    dfs()