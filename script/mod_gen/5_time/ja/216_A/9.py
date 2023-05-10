def main():
    X, Y = input().rstrip().split(".")
    Y = int(Y)
    if 0 <= Y <= 2:
        print(X + "-")
    elif 3 <= Y <= 6:
        print(X)
    else:
        print(X + "+")

if __name__ == '__main__':
    main()