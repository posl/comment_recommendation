def main():
    #入力
    X, Y = map(int, input().split())
    #処理
    for i in range(X + 1):
        if 2 * i + 4 * (X - i) == Y:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()