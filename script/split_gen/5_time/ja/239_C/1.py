def solve():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1 + y1) == (x2 + y2) or (x1 - y1) == (x2 - y2) or abs(x1 - x2) + abs(y1 - y2) <= 3:
        print("Yes")
    else:
        print("No")
    return 0
