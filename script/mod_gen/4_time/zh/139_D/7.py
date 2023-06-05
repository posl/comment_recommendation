def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return n * (n - 1) // 2
    else:
        return (n - 1) * (n - 2) // 2 + n

if __name__ == '__main__':
    solve()