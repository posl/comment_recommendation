def main():
    X = input()
    if X.find('.') != -1:
        X = X[:X.find('.')]
    print(X)

if __name__ == '__main__':
    main()