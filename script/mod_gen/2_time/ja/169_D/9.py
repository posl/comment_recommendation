def main():
    #入力
    N = int(input())
    #初期化
    count = 0
    z = 2
    #処理
    while True:
        if N == 1:
            break
        elif N % z == 0:
            N = N // z
            count += 1
        else:
            z += 1
    #出力
    print(count)

if __name__ == '__main__':
    main()