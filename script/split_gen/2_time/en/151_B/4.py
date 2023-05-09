def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if sum_A + K * (N - 1) < M * N:
        print(-1)
    else:
        print(max(0, M * N - sum_A))
