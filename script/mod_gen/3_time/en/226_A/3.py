def main():
    X = input()
    if int(X[-1]) < 5:
        print(int(X[0]))
    else:
        print(int(X[0]) + 1)

if __name__ == '__main__':
    main()