def main():
    #入力
    S = input()
    a, b = map(int, input().split())
    #文字列の入れ替え
    S = S[:a-1] + S[b-1] + S[a:b-1] + S[a-1] + S[b:]
    #出力
    print(S)

if __name__ == '__main__':
    main()