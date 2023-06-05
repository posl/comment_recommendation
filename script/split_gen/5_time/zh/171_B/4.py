def min_price(N, K, p):
    p.sort()
    return sum(p[:K])
