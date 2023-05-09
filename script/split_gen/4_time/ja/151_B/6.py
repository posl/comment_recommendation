def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if N * M - total > K:
        print(-1)
    else:
        print(max(0, N * M - total))
