def main():
    #入力
    L,R = map(int, input().split())
    #文字列
    S = 'atcoder'
    #出力
    print(S[L-1:R])

if __name__ == '__main__':
    main()