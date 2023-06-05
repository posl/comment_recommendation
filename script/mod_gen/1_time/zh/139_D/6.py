def solve(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return n * (n - 1) // 2
    else:
        return n * (n - 1) // 2 + (n - 1) // 2

if __name__ == '__main__':
    solve()