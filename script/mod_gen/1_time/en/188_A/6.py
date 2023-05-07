def main():
    X, Y = input().split()
    if (int(X) < int(Y)):
        if (int(Y) - int(X) <= 2):
            print("Yes")
        else:
            print("No")
    else:
        if (int(X) - int(Y) <= 2):
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()