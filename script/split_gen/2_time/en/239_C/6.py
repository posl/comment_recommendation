def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print("No")
        return
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x1 - dy
    y4 = y1 + dx
    if (x3 - x1) ** 2 + (y3 - y1) ** 2 == (x3 - x2) ** 2 + (y3 - y2) ** 2 and \
       (x4 - x1) ** 2 + (y4 - y1) ** 2 == (x4 - x2) ** 2 + (y4 - y2) ** 2:
        print("Yes")
    else:
        print("No")
