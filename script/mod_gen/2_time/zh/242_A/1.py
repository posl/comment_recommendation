def problems242_a(a,b,c,x):
    if x<=a:
        return 1
    elif a+1<=x and x<=b:
        return c/(b-a)
    else:
        return 0

if __name__ == '__main__':
    problems242_a()