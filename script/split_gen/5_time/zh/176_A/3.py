def problems176_a():
    N, X, T = map(int, input().split())
    print((N+X-1)//X*T)
