def main():
    #入力
    P = list(map(int,input().split()))
    #処理
    S = ['a']*26
    for i in range(26):
        S[P[i]-1] = chr(97+i)
    #出力
    print(''.join(S))

if __name__ == '__main__':
    main()