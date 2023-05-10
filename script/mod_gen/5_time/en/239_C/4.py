def main():
    x1, y1, x2, y2 = map(int, input().split())
    x = x2 - x1
    y = y2 - y1
    if x == 0 and y == 0:
        print("No")
    elif x*x + y*y == 5:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()