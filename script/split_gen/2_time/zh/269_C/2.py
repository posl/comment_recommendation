def g(a,b):
    if b==0:
        return a
    else:
        return g(b,a%b)
