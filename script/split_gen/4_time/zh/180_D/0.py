def solve(x,y,a,b):
    exp = 0
    str = x
    while True:
        if str >= y:
            break
        if str * a >= str + b:
            exp += 1
            str += b
        else:
            str *= a
    return exp
