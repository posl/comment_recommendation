def solve(x,y,a,b):
    exp = 0
    str = x
    while str<y:
        if str*a < str+b:
            str *= a
            exp += 1
        else:
            str += b
            exp += 1
    return exp
