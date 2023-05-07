def main():
    N, M, X = map(int, input().split())
    C = [0] * N
    A = [[0] * M for _ in range(N)]
    for i in range(N):
        C[i], *A[i] = map(int, input().split())
    ans = 10**10
    for i in range(2**N):
        cost = 0
        understanding = [0] * M
        for j in range(N):
            if ((i >> j) & 1):
                cost += C[j]
                for k in range(M):
                    understanding[k] += A[j][k]
        if all(u >= X for u in understanding):
            ans = min(ans, cost)
    if ans == 10**10:
        print(-1)
    else:
        print(ans)
