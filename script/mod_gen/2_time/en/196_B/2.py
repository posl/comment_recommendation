def main():
    X = input()
    if '.' in X:
        print(X[:X.find('.')])
    else:
        print(X)

if __name__ == '__main__':
    main()