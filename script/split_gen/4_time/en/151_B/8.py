def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if sum_A >= M * N:
        print(0)
    elif sum_A + K < M * N:
        print(-1)
    else:
        print(M * N - sum_A)
