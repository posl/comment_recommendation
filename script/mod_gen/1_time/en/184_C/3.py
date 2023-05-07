def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
        return
    if abs(x1 - x2) + abs(y1 - y2) <= 3:
        print(1)
        return
    if abs(x1 - x2) + abs(y1 - y2) <= 6:
        print(2)
        return
    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print(2)
        return
    if abs(x1 - x2) + abs(y1 - y2) <= 6 or abs((x1 + y1) - (x2 + y2)) <= 3 or abs((x1 - y1) - (x2 - y2)) <= 3:
        print(2)
        return
    print(3)
    return

if __name__ == '__main__':
    main()