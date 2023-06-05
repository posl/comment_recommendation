def solve(x,y,a,b):
    exp = 0
    while True:
        if x >= y:
            break
        if x * a < x + b:
            x *= a
            exp += 1
        else:
            exp += (y - x - 1) // b
            break
    return exp
