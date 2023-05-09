def solve(x, y, a, b):
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            x += b
            exp += 1
    return exp - 1

if __name__ == '__main__':
    solve()