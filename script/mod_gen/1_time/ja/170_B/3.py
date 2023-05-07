def main():
    X, Y = map(int, input().split())
    if X < 1 or X > 100 or Y < 1 or Y > 100:
        print("入力値が不正です")
        return 1
    if X >= 3:
        if (X - 3) * 2 + (X - 2) * 4 == Y:
            print("Yes")
        else:
            print("No")
    else:
        if X * 2 == Y:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()