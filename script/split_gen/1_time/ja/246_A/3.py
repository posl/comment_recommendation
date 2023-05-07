def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    if x1 != x2 and x1 != x3:
        x = x1
    elif x2 != x1 and x2 != x3:
        x = x2
    else:
        x = x3
    if y1 != y2 and y1 != y3:
        y = y1
    elif y2 != y1 and y2 != y3:
        y = y2
    else:
        y = y3
    print(x, y)
