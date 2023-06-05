def min_price(N, K, p):
    p.sort()
    return sum(p[:K])

if __name__ == '__main__':
    min_price()