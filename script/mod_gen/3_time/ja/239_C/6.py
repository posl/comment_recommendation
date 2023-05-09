def main():
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 or y1 == y2:
        print("Yes")
    elif x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()