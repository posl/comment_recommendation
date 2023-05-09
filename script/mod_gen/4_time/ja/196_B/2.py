def main():
    X = input()
    if '.' in X:
        X = X.split('.')[0]
    print(X)
    return

if __name__ == '__main__':
    main()