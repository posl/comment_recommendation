def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    x3 = x2 - dy
    y3 = y2 + dx
    x4 = x3 - dx
    y4 = y3 - dy
    print("Yes" if x3 == x4 and y3 == y4 else "No")

if __name__ == '__main__':
    main()