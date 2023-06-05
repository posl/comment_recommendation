def solve(a, n):
    if a % 2 == 0:
        return solve_even(a, n)
    else:
        return solve_odd(a, n)

if __name__ == '__main__':
    solve()