def f(a,b):
    if a == 0:
        if b == 0:
            return 0
        else:
            return f(0,b) + 1
    else:
        if b == 0:
            return f(a,0) + 1
        else:
            return f(0,b) + f(a,0)
