def solve():
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    if N * M <= total:
        print(0)
    elif N * M - total <= K:
        print(N * M - total)
    else:
        print(-1)
