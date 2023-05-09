def solve(x, a, d, n):
    # print(x, a, d, n)
    if d == 0:
        if x != a:
            return -1
        else:
            return 0
    else:
        if n % 2 == 0:
            if x < a:
                return -1
            else:
                if (x - a) % 2 == 0:
                    return 0
                else:
                    return 1
        else:
            if x < a:
                if (a - x) % 2 == 0:
                    return 1
                else:
                    return 2
            else:
                if (x - a) % 2 == 0:
                    return 1
                else:
                    return 2
