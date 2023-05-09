def solve(x, y, a, b):
    if y <= x:
        return 0
    exp = 0
    while True:
        if x*a < x+b and x*a < y:
            x *= a
            exp += 1
        else:
            exp += (y-x-1)//b
            break
    return exp

if __name__ == '__main__':
    solve()