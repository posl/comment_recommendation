def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        C[i], *A[i] = map(int, input().split())
    ans = 10**10
    for bit in range(1 << N):
        cost = 0
        level = [0] * M
        for i in range(N):
            if bit & (1 << i):
                cost += C[i]
                for j in range(M):
                    level[j] += A[i][j]
        if min(level) >= X:
            ans = min(ans, cost)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
