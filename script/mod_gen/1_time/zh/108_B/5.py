def main():
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = x2 - (y2 - y1), y2 + (x2 - x1), x1 - (y2 - y1), y1 + (x2 - x1)
    print(x3, y3, x4, y4)

if __name__ == '__main__':
    main()