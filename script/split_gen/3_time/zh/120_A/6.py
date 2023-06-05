def problem120_a():
    a,b,c = map(int,input().split())
    if a*c <= b:
        print(c)
    else:
        print(b//a)
