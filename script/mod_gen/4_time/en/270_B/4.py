def main():
    X, Y, Z = map(int, input().split())
    if X > Y and Y > Z:
        print("1")
    elif X > Y and Y < Z:
        print("-1")
    elif X < Y and Y < Z:
        print("-1")
    elif X < Y and Y > Z:
        print("-1")
    elif X > Y and Y == Z:
        print("-1")
    elif X < Y and Y == Z:
        print("-1")
    elif X == Y and Y > Z:
        print("-1")
    elif X == Y and Y < Z:
        print("-1")
    elif X == Y and Y == Z:
        print("-1")
    elif X < Y and Y == Z:
        print("-1")
    elif X > Y and Y == Z:
        print("-1")
    elif X < Y and Y == Z:
        print("-1")
    elif X > Y and Y == Z:
        print("-1")
    else:
        print("0")

if __name__ == '__main__':
    main()