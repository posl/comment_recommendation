def main():
    #入力
    P = list(map(int,input().split()))
    #辞書順で小さい方からP_i番目の英小文字をリストに格納
    S = [chr(97+i) for i in range(26)]
    S = [S[i-1] for i in P]
    #出力
    print(*S,sep="")

if __name__ == '__main__':
    main()