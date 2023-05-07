def main():
    x1, y1, x2, y2 = map(int, input().split())
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0:
        print("Yes")
    elif dy == 0:
        print("Yes")
    elif abs(dx) == abs(dy):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()