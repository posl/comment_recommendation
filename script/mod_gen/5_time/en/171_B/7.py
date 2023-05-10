def solve(N, K, p):
    p.sort()
    return sum(p[:K])

if __name__ == '__main__':
    solve()