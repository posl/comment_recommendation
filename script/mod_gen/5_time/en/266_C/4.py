def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    a = (x2-x1)*(y3-y2) - (y2-y1)*(x3-x2)
    b = (x3-x2)*(y4-y3) - (y3-y2)*(x4-x3)
    c = (x4-x3)*(y1-y4) - (y4-y3)*(x1-x4)
    d = (x1-x4)*(y2-y1) - (y1-y4)*(x2-x1)
    if a >= 0 and b >= 0 and c >= 0 and d >= 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()