def solve(n, k, h):
    h.sort()
    min_diff = h[-1] - h[0]
    for i in range(n - k + 1):
        min_diff = min(min_diff, h[i + k - 1] - h[i])
    return min_diff

if __name__ == '__main__':
    solve()