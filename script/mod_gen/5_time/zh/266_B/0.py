def solve(N):
    if N == 0:
        return 0
    else:
        return 998244353 - N % 998244353

if __name__ == '__main__':
    solve()