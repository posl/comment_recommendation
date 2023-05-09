def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) + K * (N - 1) < M * N:
        print(-1)
        return
    print(max(M * N - sum(A), 0))
