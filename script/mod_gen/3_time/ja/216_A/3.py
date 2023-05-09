def main():
    X, Y = input().split(".")
    if Y in ["0", "1", "2"]:
        print(X + "-")
    elif Y in ["3", "4", "5", "6"]:
        print(X)
    else:
        print(X + "+")

if __name__ == '__main__':
    main()