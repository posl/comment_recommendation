def main():
    X, Y = map(int, input().split())
    if X * 4 >= Y and Y >= X * 2:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()