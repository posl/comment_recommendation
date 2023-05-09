def solve(x, a, d, n):
    if d == 0:
        if x == a:
            return 0
        else:
            return 1
    else:
        if x == a:
            return 0
        else:
            if (x - a) % d == 0:
                return abs((x - a) // d)
            else:
                return abs((x - a) // d) + 1
