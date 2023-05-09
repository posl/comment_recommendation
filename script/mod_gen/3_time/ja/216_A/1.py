def main():
    x, y = input().split(".")
    x = int(x)
    y = int(y)
    if 0 <= y <= 2:
        print(x - 1)
    elif 3 <= y <= 6:
        print(x)
    else:
        print(x + 1)

if __name__ == '__main__':
    main()