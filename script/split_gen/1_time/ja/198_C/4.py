def solve():
    r,x,y = list(map(int,input().split()))
    if r**2 == x**2 + y**2:
        print(1)
        return
    if r**2 > x**2 + y**2:
        print(2)
        return
    print(math.ceil((x**2 + y**2)**(1/2)/r))
