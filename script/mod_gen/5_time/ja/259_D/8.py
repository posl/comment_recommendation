def f():
    import sys
    import math
    input = sys.stdin.readline
    def is_cross(x1, y1, r1, x2, y2, r2):
        d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
        if d < r1+r2 and d > abs(r1-r2):
            return True
        else:
            return False
    n = int(input())
    sx, sy, tx, ty = map(int, input().split())
    if sx == tx and sy == ty:
        print("Yes")
        exit()
    xl = []
    yl = []
    rl = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        xl.append(x)
        yl.append(y)
        rl.append(r)
    for i in range(n):
        if is_cross(sx, sy, rl[i], tx, ty, 0):
            print("Yes")
            exit()
    for i in range(n):
        for j in range(i+1, n):
            if is_cross(xl[i], yl[i], rl[i], xl[j], yl[j], rl[j]):
                print("Yes")
                exit()
    print("No")
f()
