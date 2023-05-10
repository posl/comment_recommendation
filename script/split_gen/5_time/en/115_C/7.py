def solve(n, k, h):
    h.sort()
    return h[k-1] - h[0]
