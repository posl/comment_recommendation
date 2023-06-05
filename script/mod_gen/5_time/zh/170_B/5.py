def main():
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if Y % 2 == 0 and Y >= 2 * X and Y <= 4 * X:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()