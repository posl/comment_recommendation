def main():
    X, Y, Z = map(int, input().split())
    if abs(X) > abs(Y):
        print(abs(X) + abs(X - Z))
    else:
        print(abs(X) + abs(Y) + abs(Y - Z))

if __name__ == '__main__':
    main()