def main():
    x1, y1, x2, y2 = map(int, input().split())
    if abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2 == 10:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()