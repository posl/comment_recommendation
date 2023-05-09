def main():
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [[0]*(N-K+1) for _ in range(N-K+1)]
    for i in range(N-K+1):
        for j in range(N-K+1):
            B[i][j] = A[i][j]
    for i in range(N-K+1):
        for j in range(N-K+1):
            for k in range(K):
                for l in range(K):
                    B[i][j] = max(B[i][j], A[i+k][j+l])
    for i in range(N-K+1):
        for j in range(N-K+1):
            for k in range(K):
                for l in range(K):
                    B[i][j] = min(B[i][j], A[i+k][j+l])
    for i in range(N-K+1):
        for j in range(N-K+1):
            print(B[i][j], end=" ")
        print()
