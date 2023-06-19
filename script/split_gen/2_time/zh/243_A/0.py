def solve():
    v,a,b,c = map(int,input().split())
    while v > 0:
        v -= a
        if v <= 0:
            print("T")
            break
        v -= b
        if v <= 0:
            print("M")
            break
        v -= c
        if v <= 0:
            print("F")
            break
