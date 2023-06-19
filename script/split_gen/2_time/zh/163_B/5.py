def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    if sum(A) > N:
        print(-1)
        return
    print(N - sum(A))
