def solve():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    if sum(A) <= N:
        print(N-sum(A))
    else:
        print(-1)
