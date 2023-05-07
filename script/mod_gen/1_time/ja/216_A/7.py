def main():
    X, Y = input().split(".")
    Y = int(Y[0])
    if Y <= 2:
        print(X + "-")
    elif Y <= 6:
        print(X)
    else:
        print(X + "+")
main()

if __name__ == '__main__':
    main()