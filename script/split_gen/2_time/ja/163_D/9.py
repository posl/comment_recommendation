def calc(n, k):
    if k == 1:
        return n
    else:
        return (n-k+1)*calc(n, k-1) % (10**9+7)
