def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    if d > 0:
        if a > x:
            return 1
        else:
            if (x - a) % d == 0:
                return 0
            else:
                return 1
    if d < 0:
        if a < x:
            return 1
        else:
            if (x - a) % d == 0:
                return 0
            else:
                return 1

if __name__ == '__main__':
    solve()