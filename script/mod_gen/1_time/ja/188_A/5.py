def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if X - Y < 3:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()