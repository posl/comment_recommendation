def problems242_a(a,b,c,x):
    if x<=a:
        return 1
    elif a+1<=x and x<=b:
        return c/(b-a)
    else:
        return 0
