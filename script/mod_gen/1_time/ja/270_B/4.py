def main():
    X, Y, Z = map(int, input().split())
    if X < Y and Z < Y:
        print(Y - X)
    elif X < Y and Y < Z:
        print(Z - X)
    elif Y < X and Z < X:
        print(X - Y)
    else:
        print(-1)

if __name__ == '__main__':
    main()