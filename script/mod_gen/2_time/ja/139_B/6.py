def main():
    # 標準入力からAとBを取得
    A, B = map(int, input().split())
    # AをBで割った余りを取得
    remainder = B % A
    # 余りが0でない場合は、余りをAに加算して、商に1を足す
    if remainder != 0:
        A += remainder
        B = B // A + 1
    # 余りが0の場合は、商に1を足す
    else:
        B = B // A
    # 商を出力
    print(B)

if __name__ == '__main__':
    main()