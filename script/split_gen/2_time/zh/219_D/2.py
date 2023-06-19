def get_input():
    n = int(input())
    x,y = input().split()
    x = int(x)
    y = int(y)
    a = []
    b = []
    for i in range(n):
        ai,bi = input().split()
        a.append(int(ai))
        b.append(int(bi))
    return n,x,y,a,b
