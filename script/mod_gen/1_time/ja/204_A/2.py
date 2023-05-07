def main():
    x, y = map(int, input().split())
    if x == y:
        print(x)
    elif x == 0 and y == 1 or x == 1 and y == 2 or x == 2 and y == 0:
        print(2)
    else:
        print(0)

if __name__ == '__main__':
    main()