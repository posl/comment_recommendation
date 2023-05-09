def solve(x, y, a, b):
    exp = 0
    while x*a <= x+b and x*a < y:
        x *= a
        exp += 1
    exp += (y-x-1)//b
    return exp

if __name__ == '__main__':
    solve()