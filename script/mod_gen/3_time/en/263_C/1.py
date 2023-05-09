def dfs(x, N, M):
    if x == N:
        print(*A)
        return
    for i in range(A[x-1]+1, M+1):
        A[x] = i
        dfs(x+1, N, M)
N, M = map(int, input().split())
A = [0] * N
dfs(0, N, M)

if __name__ == '__main__':
    dfs()