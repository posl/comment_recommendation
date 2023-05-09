def main():
    X = input()
    if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
        print("Weak")
    elif int(X[0]) + 1 == int(X[1]) and int(X[1]) + 1 == int(X[2]) and int(X[2]) + 1 == int(X[3]):
        print("Weak")
    elif int(X[0]) == 9 and int(X[1]) == 0 and int(X[2]) == 1 and int(X[3]) == 2:
        print("Weak")
    else:
        print("Strong")

if __name__ == '__main__':
    main()