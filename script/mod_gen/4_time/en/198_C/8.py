def solve(r, x, y):
    from math import sqrt
    d = sqrt(x**2 + y**2)
    if d < r:
        return 2
    return int(d/r)+1

if __name__ == '__main__':
    solve()