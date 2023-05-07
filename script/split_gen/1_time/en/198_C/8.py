def solve():
    #import sys
    #input = sys.stdin.readline
    r,x,y = map(int,input().split())
    if r**2 > x**2 + y**2:
        print(2)
    else:
        print((x**2 + y**2)**(1/2)//r + 1)
