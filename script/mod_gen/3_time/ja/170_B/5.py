def main():
    X, Y = map(int, input().split())
    if X * 4 < Y or Y % 2 != 0:
        print("No")
    else:
        if X * 2 <= Y:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()