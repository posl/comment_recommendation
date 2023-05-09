def main():
    N, M = map(int, input().split())
    A = [1] * N
    def dfs(i):
        if i == N:
            print(*A)
            return
        for j in range(A[i - 1], M + 1):
            A[i] = j
            dfs(i + 1)
    dfs(1)
