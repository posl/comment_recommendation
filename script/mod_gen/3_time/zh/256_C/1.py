def f(h1, h2, h3, w1, w2, w3):
    import math
    from functools import reduce
    from itertools import permutations
    def comb(n, r):
        if n == 0 or r == 0:
            return 1
        else:
            return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    def comb_with_repetition(n, r):
        return comb(n + r - 1, r)
    def perm(n, r):
        return math.factorial(n) // math.factorial(n - r)
    def perm_with_repetition(n, r):
        return n ** r
    def m(n, r):
        return reduce(lambda x, y: x * y, range(n, n - r, -1), 1)

if __name__ == '__main__':
    f()