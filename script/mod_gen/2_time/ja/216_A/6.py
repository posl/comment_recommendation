def main():
    x, y = map(int, input().split("."))
    y = int(y)
    if y >= 0 and y <= 2:
        print(x - 1)
    elif y >= 3 and y <= 6:
        print(x)
    elif y >= 7 and y <= 9:
        print(x + 1)

if __name__ == '__main__':
    main()