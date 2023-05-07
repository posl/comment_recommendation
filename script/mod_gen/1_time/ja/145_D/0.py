def main():
    X, Y = map(int, input().split())
    if (X + Y) % 3 != 0:
        print(0)
        return
    if X > 2 * Y or Y > 2 * X:
        print(0)
        return
    if X == 0 and Y == 0:
        print(1)
        return
    if X == 0 or Y == 0:
        print(1)
        return
    if X == Y:
        print(2)
        return
    print(0)

if __name__ == '__main__':
    main()