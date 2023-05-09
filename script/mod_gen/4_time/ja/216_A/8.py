def main():
    # input
    X,Y = input().split(".")
    X = int(X)
    Y = int(Y)
    # compute
    # output
    if 0 <= Y and Y <= 2:
        print(str(X) + "-")
    elif 3 <= Y and Y <= 6:
        print(X)
    else:
        print(str(X) + "+")

if __name__ == '__main__':
    main()