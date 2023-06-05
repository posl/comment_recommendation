def solve(n, a, b, c, ls):
    if n == 1:
        return abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[0])
    if n == 2:
        return min(abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[0]))
    if n == 3:
        return min(abs(a - ls[0]) + abs(b - ls[1]) + abs(c - ls[2]),
                   abs(a - ls[0]) + abs(b - ls[2]) + abs(c - ls[1]),
                   abs(a - ls[1]) + abs(b - ls[0]) + abs(c - ls[2]),
                   abs(a - ls[1]) + abs(b - ls[2]) + abs(c - ls[0]),
                   abs(a - ls[2]) + abs(b - ls[0]) + abs(c - ls[1]),
                   abs(a - ls[2]) + abs(b - ls[1]) + abs(c - ls[0]),
                   abs(a - ls[0]) + abs(b - ls[0]) + abs(c - ls[2]),
                   abs(a - ls[0]) + abs(b - ls[2]) + abs(c - ls[0]),
                   abs(a - ls[2]) + abs(b - ls[0]) + abs(c - ls[0]),
                   abs(a - ls[1]) + abs(b - ls[1]) + abs(c - ls[2]),
                   abs(a - ls[1]) + abs(b - ls[2]) + abs(c - ls[1]),
                   abs(a - ls[2]) + abs(b - ls[1]) + abs(c - ls[1]),
                   abs(a - ls[0
