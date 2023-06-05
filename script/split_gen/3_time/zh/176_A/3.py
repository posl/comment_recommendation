def problem176_a():
    n,x,t = map(int,input().split())
    if n%x != 0:
        print((n//x+1)*t)
    else:
        print((n//x)*t)
