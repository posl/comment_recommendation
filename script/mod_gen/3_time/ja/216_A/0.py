def main():
    X, Y = map(int, input().split("."))
    if 0 <= Y <= 2:
        print(X, "-", sep="")
    elif 3 <= Y <= 6:
        print(X)
    else:
        print(X, "+", sep="")

if __name__ == '__main__':
    main()