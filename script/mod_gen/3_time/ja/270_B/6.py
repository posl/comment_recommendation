def main():
    #入力
    X, Y, Z = map(int, input().split())
    #出力
    if X < Y < Z:
        print(-1)
    elif X > Y > Z:
        print(-1)
    else:
        print(abs(X - Y) + abs(Y - Z))

if __name__ == '__main__':
    main()