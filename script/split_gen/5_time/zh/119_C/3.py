def solve(n, a, b, c, ls):
    #print(n, a, b, c, ls)
    if n == 1:
        return abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[0])
    elif n == 2:
        return min(abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[0]))
    else:
        return min(solve(n - 1, a, b, c, ls[:n - 1]) + abs(c - ls[n - 1]),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(b - ls[n - 1]),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a - ls[n - 1]),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a + b - ls[n - 1] * 2),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a + c - ls[n - 1] * 2),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(b + c - ls[n - 1] * 2),
                   solve(n - 1, a, b, c, ls[:n - 1]) + abs(a + b + c - ls[n - 1] * 3),
                   solve(n - 1, a, b, c, ls[:n - 1]))
