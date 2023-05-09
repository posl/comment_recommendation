def solve(x, a, d, n):
    if (x - a) % d != 0:
        return -1
    else:
        return (x - a) // d + 1

if __name__ == '__main__':
    solve()