def problems100_b():
    D,N = map(int,input().split())
    if N == 100:
        N = 101
    print(100**D*N)
