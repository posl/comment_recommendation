def findMinPrice(N, K, p):
    p.sort()
    return sum(p[:K])
