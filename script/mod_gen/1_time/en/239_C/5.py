def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x1 - x2
    y = y1 - y2
    if x * x + y * y == 5:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()