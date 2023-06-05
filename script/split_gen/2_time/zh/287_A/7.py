def solve():
    n,x = map(int,input().split())
    a = []
    b = []
    for i in range(n):
        ai,bi = map(int,input().split())
        a.append(ai)
        b.append(bi)
    #print(n,x,a,b)
    #print(sum([a[i]*b[i] for i in range(n)]))
    if sum([a[i]*b[i] for i in range(n)]) >= x:
        print("Yes")
    else:
        print("No")
