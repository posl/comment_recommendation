def solve(n):
    if n == 1:
        return 'A'
    elif n == 2:
        return 'B'
    elif n % 2 == 0:
        return solve(n // 2) + 'B'
    else:
        return solve(n - 1) + 'A'

if __name__ == '__main__':
    solve()