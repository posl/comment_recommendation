def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum_A = sum(A)
    if M * N - sum_A > K:
        print(-1)
    else:
        print(max(M * N - sum_A, 0))
