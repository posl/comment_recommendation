def main():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if total >= N * M:
        print(0)
    elif total + K < N * M:
        print(-1)
    else:
        print(N * M - total)
