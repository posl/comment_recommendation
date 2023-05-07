def main():
    #入力
    s = input()
    #初期化
    ans = 0
    #処理
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            ans += 2
    #出力
    print(ans)

if __name__ == '__main__':
    main()