def problem():
    x, a, d, n = map(int, input().split())
    if d == 0:
        if a == x:
            return 0
        else:
            return 1
    if (x - a) % d == 0:
        if 1 <= (x - a) // d <= n:
            return 0
        else:
            return 1
    else:
        if 1 <= (x - a) // d + 1 <= n:
            return 1
        else:
            if 1 <= (x - a) // d - 1 <= n:
                return 1
            else:
                return 2
print(problem())
