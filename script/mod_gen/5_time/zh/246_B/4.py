def problems246_b():
    import sys
    import math
    #sys.stdin = open("data/246_b.txt", "r")
    a, b = map(int, input().split())
    #print(a, b)
    #print(math.sqrt(a*a + b*b))
    x = a / math.sqrt(a*a + b*b)
    y = b / math.sqrt(a*a + b*b)
    print(x, y)
problems246_b()
