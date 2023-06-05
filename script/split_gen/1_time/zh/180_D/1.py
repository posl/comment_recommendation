def problems180_d(x,y,a,b):
    exp = 0
    str = x
    while True:
        if str * a <= str + b:
            exp += 1
            str *= a
        else:
            break
        if str >= y:
            break
    exp += (y - str - 1) // b
    return exp
