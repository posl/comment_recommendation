def solve():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 - x2)**2 + (y1 - y2)**2 == (x1 - y1)**2 or (x1 - x2)**2 + (y1 - y2)**2 == (x1 + y1)**2:
        print("Yes")
    else:
        print("No")
