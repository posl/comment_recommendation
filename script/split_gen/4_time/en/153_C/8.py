def problems153_c():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    #print(H)
    if K == 0:
        print(sum(H))
    else:
        print(sum(H[:-K]))
