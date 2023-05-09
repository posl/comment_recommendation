def main():
    #atcoderの文字列を定義
    atcoder = "atcoder"
    #入力
    L,R = map(int,input().split())
    #L文字目からR文字目までを出力
    print(atcoder[L-1:R])

if __name__ == '__main__':
    main()