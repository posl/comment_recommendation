def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3 = x2 - x1
    y3 = y2 - y1
    x4 = -y3
    y4 = x3
    x5 = x4 + x1
    y5 = y4 + y1
    print("Yes" if (x5, y5) != (x2, y2) else "No")

if __name__ == '__main__':
    main()