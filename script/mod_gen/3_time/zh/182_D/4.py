def solve(n, a):
    s = 0
    max_s = 0
    for i in range(n):
        s += a[i]
        max_s = max(max_s, s)
    return max_s

if __name__ == '__main__':
    solve()