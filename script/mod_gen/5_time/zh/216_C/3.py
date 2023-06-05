def solve(n):
    s = ''
    while n > 0:
        if n % 2 == 0:
            n = n // 2
            s += 'B'
        else:
            n -= 1
            s += 'A'
    return s[::-1]

if __name__ == '__main__':
    solve()