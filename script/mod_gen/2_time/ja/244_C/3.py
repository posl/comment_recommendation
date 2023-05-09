def main():
    N = int(input())
    # 1 以上 2N+1 以下の整数を 1 つずつ宣言する
    for i in range(1, 2 * N + 2):
        print(i)
        # flushする
        sys.stdout.flush()
        # 青木君が宣言する整数を受け取る
        a = int(input())
        # 青木君が宣言した整数が 0 なら終了
        if a == 0:
            break

if __name__ == '__main__':
    main()