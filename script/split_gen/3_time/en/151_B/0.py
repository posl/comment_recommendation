def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) + K * N < M * N:
        print(-1)
    else:
        print(max(0, M * N - sum(A)))
