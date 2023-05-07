def main():
    X, Y = map(int, input().split())
    if X > Y:
        if X - Y > 2:
            print("No")
        else:
            print("Yes")
    else:
        if Y - X > 2:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()