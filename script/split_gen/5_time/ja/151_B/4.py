def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    if N*M - sum <= K:
        print(max(N*M - sum, 0))
    else:
        print(-1)
