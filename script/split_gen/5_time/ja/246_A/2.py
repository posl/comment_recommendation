def main():
    # input
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    # compute
    if x1 == x2:
        x = x3
    elif x2 == x3:
        x = x1
    else:
        x = x2
    if y1 == y2:
        y = y3
    elif y2 == y3:
        y = y1
    else:
        y = y2
    # output
    print(x, y)
