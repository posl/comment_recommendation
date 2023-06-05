def get_input():
    n = int(input())
    x,y = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    return n,x,y,a,b
