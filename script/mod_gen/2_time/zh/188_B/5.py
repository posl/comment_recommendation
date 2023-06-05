def main():
    X, Y = map(int, input().split())
    if X < Y:
        X, Y = Y, X
    if X - Y < 3:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()