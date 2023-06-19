def comb(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    over = reduce(lambda a, b: a*b, xrange(n, n-r, -1))
    under = reduce(lambda a, b: a*b, xrange(1, r+1))
    return over/under
l = input()
print comb(l-1, 11)
