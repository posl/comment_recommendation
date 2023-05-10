def solve(n, k, h):
    h.sort()
    return h[k-1] - h[0]

if __name__ == '__main__':
    solve()