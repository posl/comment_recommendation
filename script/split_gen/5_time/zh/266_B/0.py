def solve(N):
    if N == 0:
        return 0
    else:
        return 998244353 - N % 998244353
