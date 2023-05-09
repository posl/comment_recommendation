def main():
    #入力
    a, n = map(int, input().split())
    #初期値
    x = 1
    cnt = 0
    #処理
    while x < n:
        #a倍する
        x *= a
        cnt += 1
        #10で割り切れないなら
        if x % 10 != 0:
            #末尾の数字を先頭に持ってくる
            x = int(str(x)[-1] + str(x)[:-1])
            cnt += 1
    #出力
    if x == n:
        print(cnt)
    else:
        print(-1)

if __name__ == '__main__':
    main()