def main():
    #入力
    L, R = map(int, input().split())
    S = input()
    #処理
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    #出力
    print(S)

if __name__ == '__main__':
    main()