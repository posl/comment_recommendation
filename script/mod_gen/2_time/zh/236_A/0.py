def solve(a, n):
    if a == 2:
        return solve2(a, n)
    else:
        return solve3(a, n)

if __name__ == '__main__':
    solve()