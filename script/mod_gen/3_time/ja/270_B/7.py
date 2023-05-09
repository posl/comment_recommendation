def main():
    #入力
    X, Y, Z = map(int, input().split())
    #処理
    if abs(X) < abs(Y):
        if abs(X) < abs(Z):
            print(abs(X) + abs(Z))
        else:
            print(abs(X) + abs(Y))
    else:
        if abs(Y) < abs(Z):
            print(abs(Y) + abs(Z))
        else:
            print(abs(X) + abs(Y))

if __name__ == '__main__':
    main()