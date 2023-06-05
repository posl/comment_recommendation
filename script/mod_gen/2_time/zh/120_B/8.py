def solve(a, b, c):
    if a * c <= b:
        return c
    else:
        return b // a

if __name__ == '__main__':
    solve()