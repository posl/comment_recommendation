def main():
    # 入力
    X, Y = map(int, input().split())
    # 処理
    if 4 * X < Y or Y < 2 * X:
        print("No")
    elif Y % 2 == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()