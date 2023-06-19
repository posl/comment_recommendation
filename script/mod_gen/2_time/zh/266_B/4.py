def solve(n):
    return (998244353 - (n % 998244353)) % 998244353

if __name__ == '__main__':
    solve()