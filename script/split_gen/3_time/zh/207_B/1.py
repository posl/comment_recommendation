def solve():
    a,b,c,d = map(int, input().split())
    if a < b:
        print(-1)
    else:
        if d == 1:
            print(0)
        else:
            x = (a * d - a) // (b * d - c)
            if (a * d - a) % (b * d - c) != 0:
                x += 1
            print(x)
