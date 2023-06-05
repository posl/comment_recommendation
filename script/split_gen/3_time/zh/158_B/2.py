def problems158_b():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
        return
    if a+b >= n:
        print(a)
        return
    else:
        print(a+(n-a-b))
