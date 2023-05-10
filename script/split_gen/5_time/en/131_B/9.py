def solve(n, l):
    return sum(l) - min(l, key=abs)
