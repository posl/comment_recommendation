def problem198_c():
    r,x,y = map(int, input().split())
    if r*r == (x*x + y*y):
        print(1)
    elif r*r > (x*x + y*y):
        print(2)
    else:
        print(int(((x*x + y*y)**(1/2) + r -1)/r))
    return
