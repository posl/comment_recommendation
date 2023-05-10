def solve(n):
    if n % 2 == 0:
        return n // 2 - 1
    else:
        return n // 2

if __name__ == '__main__':
    solve()