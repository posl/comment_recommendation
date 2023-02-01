#問題文
#英小文字、,、" からなる長さ N の文字列 S が与えられます。S に含まれる " の個数は偶数であることが保証されています。
#S に含まれる " の個数を 2K 個とすると、各 i=1,2,…,K について 2i−1 番目の " から 2i 番目の " までの文字のことを 括られた文字 と呼びます。
#あなたの仕事は、 S に含まれる , のうち、括られた文字 でないもの を . で置き換えて得られる文字列を答えることです。
#
#制約
#N は 1 以上 2×10^5以下の整数
#S は英小文字、,、" からなる長さ N の文字列
#S に含まれる " の個数は偶数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#N
#S
#
#出力
#答えを出力せよ。
#
#入力例1
#8
#"a,b"c,d
#
#出力例1
#"a,b"c.d
#
#入力例2
#5
#'''''
#
#出力例2
#.....
#
#入力例3
#20
#a,"t,"c,"o,"d,"e,"r,
#
#出力例3
#a."t,"c."o,"d."e,"r.

def main():
    N = int(input())
    S = input()
    ans = ''
    flag = False
    for i in range(N):
        if S[i] == '"':
            flag = not flag
        elif S[i] == ',' and flag:
            ans += '.'
        else:
            ans += S[i]
    print(ans)

if __name__ == '__main__':
    main()