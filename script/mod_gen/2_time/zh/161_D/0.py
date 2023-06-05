def solve(n, k):
    return min(n % k, k - (n % k))

if __name__ == '__main__':
    solve()