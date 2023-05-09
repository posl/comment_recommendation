def main():
    X,Y = map(int,input().split("."))
    if Y <= 2:
        print("{}-".format(X))
    elif Y <= 6:
        print(X)
    else:
        print("{}+".format(X))

if __name__ == '__main__':
    main()