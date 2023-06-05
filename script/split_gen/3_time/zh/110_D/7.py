def f(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return x*f(x-1)
