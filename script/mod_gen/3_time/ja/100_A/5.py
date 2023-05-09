def main():
    # 標準入力から A, B を取得する
    A, B = map(int, input().split())
    # A+B が 16 以下であれば Yay! を返す
    if A+B <= 16:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()