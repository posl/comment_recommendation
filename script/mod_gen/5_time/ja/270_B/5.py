def main():
    X, Y, Z = map(int, input().split())
    if Y > Z:
        print(-1)
    else:
        print(X // (Z - Y) - (X % (Z - Y) == 0))

if __name__ == '__main__':
    main()