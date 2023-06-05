def solve(n):
    if n == 1:
        return 'A'
    elif n % 2 == 0:
        return 'B' + solve(n // 2)
    else:
        return 'A' + solve(n - 1)

if __name__ == '__main__':
    solve()