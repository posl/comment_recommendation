def solve(n, m, a):
    a = sorted(a, reverse=True)
    total = sum(a[:m])
    return total + m * m

if __name__ == '__main__':
    solve()