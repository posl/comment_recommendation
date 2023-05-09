def solve(x, y, a, b):
    exp = 0
    while (a*x) < (x + b) and x < y:
        x *= a
        exp += 1
    exp += (y - x - 1) // b
    return exp

if __name__ == '__main__':
    solve()