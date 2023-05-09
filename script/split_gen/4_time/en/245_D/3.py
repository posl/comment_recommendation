def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (M + 1)
    for i in range(N + M):
        for j in range(M + 1):
            if 0 <= i - j <= N:
                B[j] += A[i - j] * C[i]
    print(*B)
