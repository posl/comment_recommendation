def main():
    import sys
    import math
    n = int(sys.stdin.readline())
    x0,y0 = map(int,sys.stdin.readline().split())
    x1,y1 = map(int,sys.stdin.readline().split())
    x2,y2 = map(int,sys.stdin.readline().split())
    x3,y3 = map(int,sys.stdin.readline().split())
    if x0 == x2:
        x4 = x1
    elif x0 == x1:
        x4 = x2
    else:
        x4 = x0
    if y0 == y2:
        y4 = y1
    elif y0 == y1:
        y4 = y2
    else:
        y4 = y0
    if x3 == x2:
        x5 = x1
    elif x3 == x1:
        x5 = x2
    else:
        x5 = x3
    if y3 == y2:
        y5 = y1
    elif y3 == y1:
        y5 = y2
    else:
        y5 = y3
    if x4 == x5:
        if x4 == x0:
            x1 = x2
        else:
            x1 = x0
        if y4 == y0:
            y1 = y2
        else:
            y1 = y0
    else:
        if x4 == x0:
            x1 = x5
        else:
            x1 = x4
        if y4 == y0:
            y1 = y5
        else:
            y1 = y4
    print(x1,y1)
main()

if __name__ == '__main__':
    main()