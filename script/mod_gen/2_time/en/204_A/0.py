def main():
    x, y = map(int, input().split())
    if x == 0:
        if y == 1:
            print(2)
        else:
            print(0)
    elif x == 1:
        if y == 2:
            print(0)
        else:
            print(1)
    else:
        if y == 0:
            print(1)
        else:
            print(2)

if __name__ == '__main__':
    main()