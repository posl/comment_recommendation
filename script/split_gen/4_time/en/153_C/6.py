def solve():
    N,K=map(int,input().split())
    H=list(map(int,input().split()))
    H.sort()
    if K>=N:
        print(0)
        return
    print(sum(H[:N-K]))
