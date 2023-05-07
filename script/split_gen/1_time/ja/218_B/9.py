def main():
    #入力
    P = list(map(int,input().split()))
    #辞書順のアルファベットをリスト化
    alpha = list(map(chr, range(97, 123)))
    #出力
    for i in range(len(P)):
        print(alpha[P[i]-1],end="")
