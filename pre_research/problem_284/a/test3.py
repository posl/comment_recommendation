#問題文
#N個の文字列S1, S2, …, SNがこの順番で与えられます．
#SN, SN - 1, …, S1の順番で出力してください．
#
#制約
#1 ≦ N ≦ 10
#Nは整数
#Siは英小文字，英大文字，数字からなる長さ1以上10以下の文字列
#
#入力
#入力は以下の形式で標準入力から与えられる．
#N
#S1
#S2
#.
#.
#.
#SN
#
#出力
#N行出力せよ．i(1 ≦ i ≦ N)行目には，SN+1-iを出力せよ
#
#入力例１
#3
#Takahashi
#Aoki
#Snuke
#
#出力例１
#Snuke
#Aoki
#Takahashi
#
#入力例２
#4
#2023
#Year
#New
#Happy
#
#出力例２
#Happy
#New
#Year
#2023

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        print(S[N-1-i])

if __name__ == '__main__':
    main()