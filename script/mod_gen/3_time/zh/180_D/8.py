def solve(x, y, a, b):
    exp = 0
    while x < y:
        if x * a < x + b:
            x *= a
        else:
            x += b
        exp += 1
    return exp

if __name__ == '__main__':
    solve()