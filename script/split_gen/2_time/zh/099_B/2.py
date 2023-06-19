def solve():
    a,b = map(int,input().split())
    h = b - a
    x = 1
    while x*(x+1)//2 < h:
        x += 1
    print(x*(x+1)//2 - h)
