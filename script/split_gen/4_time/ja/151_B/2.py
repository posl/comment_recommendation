def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N-1):
        sum += A[i]
    if N*M - sum > K:
        print(-1)
    else:
        print(max(0, N*M - sum))
