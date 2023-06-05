def drink_sound():
    a,b,c = map(int,input().split())
    if a>b:
        print(0)
    else:
        print(min(b//a,c))
