def f(a,b):
    if a==b:
        return a
    elif a==b-1:
        return a^b
    else:
        return f(a,b-1)^b
