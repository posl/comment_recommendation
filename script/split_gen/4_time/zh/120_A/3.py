def solve():
    a,b,c = map(int,input().split())
    if a > b:
        print(0)
    else:
        print(b // a if b // a < c else c)
