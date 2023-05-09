def main():
    X, Y = map(int, input().split("."))
    if Y <= 2:
        print(X, "-", sep="")
    elif Y <= 6:
        print(X)
    else:
        print(X, "+", sep="")
main()

if __name__ == '__main__':
    main()