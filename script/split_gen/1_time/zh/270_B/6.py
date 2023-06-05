def solve():
    x,y,z = map(int, input().split())
    if x > y:
        print(z + x - y)
    else:
        print(-1)
