def main():
    # 1行目の入力
    X, Y = map(int, input().split())
    # ここに処理を書く
    if X >= Y:
        print(0)
    else:
        print((Y - X + 9) // 10)

if __name__ == '__main__':
    main()