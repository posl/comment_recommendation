def main():
    X = input()
    if '.' in X:
        print(X.split('.')[0])
    else:
        print(X)

if __name__ == '__main__':
    main()