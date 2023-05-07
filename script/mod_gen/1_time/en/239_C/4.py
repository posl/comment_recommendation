def main():
    x1, y1, x2, y2 = map(int, input().split())
    if (x1, y1) == (x2, y2):
        print("No")
        return
    if (x1 - x2) % 2 == 0:
        print("Yes")
        return
    if (y1 - y2) % 2 == 0:
        print("Yes")
        return
    print("No")

if __name__ == '__main__':
    main()