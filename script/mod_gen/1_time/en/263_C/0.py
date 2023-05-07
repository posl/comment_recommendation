def solve(n, m):
    if n == 1:
        return [[i] for i in range(1, m + 1)]
    else:
        return [[i] + j for i in range(1, m + 1) for j in solve(n - 1, m) if i < j[0]]

if __name__ == '__main__':
    solve()