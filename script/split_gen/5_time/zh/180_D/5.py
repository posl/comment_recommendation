def f(x,y,a,b):
    exp = 0
    str = x
    while str < y:
        if str * a < str + b:
            str = str * a
        else:
            str = str + b
        exp += 1
    return exp
x,y,a,b = map(int, input().split())
print(f(x,y,a,b))
