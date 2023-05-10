def solve(x, y, a, b):
    exp = 0
    while True:
        if x*a >= y:
            break
        if x*a < x+b:
            exp += 1
            x *= a
        else:
            exp += (y-x)//b
            break
    return exp
