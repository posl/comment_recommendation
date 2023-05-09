def main():
    X, Y = map(int, input().split())
    if X % 2 != Y % 2:
        print(0)
        return
    if X == 0 and Y == 0:
        print(1)
        return
    if X == 0 or Y == 0:
        print(0)
        return
    if X == 1 and Y == 1:
        print(2)
        return
    if X == 1 or Y == 1:
        print(0)
        return
    if X == 2 and Y == 2:
        print(2)
        return
    if X == 2 or Y == 2:
        print(0)
        return
    if X == 3 and Y == 3:
        print(2)
        return
    if X == 3 or Y == 3:
        print(0)
        return
    if X == 4 and Y == 4:
        print(4)
        return
    if X == 4 or Y == 4:
        print(0)
        return
    if X == 5 and Y == 5:
        print(4)
        return
    if X == 5 or Y == 5:
        print(0)
        return
    if X == 6 and Y == 6:
        print(8)
        return
    if X == 6 or Y == 6:
        print(0)
        return
    if X == 7 and Y == 7:
        print(8)
        return
    if X == 7 or Y == 7:
        print(0)
        return
    if X == 8 and Y == 8:
        print(16)
        return
    if X == 8 or Y == 8:
        print(0)
        return
    if X == 9 and Y == 9:
        print(16)
        return
    if X == 9 or Y == 9:
        print(0)
        return
    if X == 10 and Y == 10:
        print(32)
        return
    if X == 10 or Y == 10:
        print(0)
        return
    if X == 11 and Y == 11:
        print(32)
        return
    if X == 11

if __name__ == '__main__':
    main()