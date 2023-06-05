def solve(N, K, H):
    H.sort()
    #print(H)
    print(sum(H[:-K]) if K < N else 0)
