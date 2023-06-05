def solve():
    N,K = map(int,input().split())
    H = list(map(int,input().split()))
    H = sorted(H,reverse=True)
    if K >= N:
        print(0)
        return
    else:
        print(sum(H[K:]))
