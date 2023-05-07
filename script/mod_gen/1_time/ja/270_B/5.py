def main():
    # 入力
    X, Y, Z = map(int, input().split())
    # 出力
    if X < Y < Z or Z < Y < X:
        print(abs(X - Y) + abs(Y - Z))
    else:
        print(-1)

if __name__ == '__main__':
    main()