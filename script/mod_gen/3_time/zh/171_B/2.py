def findMinPrice(N, K, p):
    p.sort()
    return sum(p[:K])

if __name__ == '__main__':
    findMinPrice()