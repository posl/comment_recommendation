def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 or y1 == y2:
        print("No")
        return
    x3 = x2 - (y2 - y1)
    y3 = y2 + (x2 - x1)
    x4 = x1 - (y2 - y1)
    y4 = y1 + (x2 - x1)
    print("Yes")
    print(x3, y3, x4, y4)
