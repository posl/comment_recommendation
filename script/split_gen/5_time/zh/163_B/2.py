def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    print(N-sum(A) if N>=sum(A) else -1)
