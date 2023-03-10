#問題文
#正整数Nが与えられます。N は、2 つの相異なる素数 p,q を用いて N=p^2 * qと表せることがわかっています。
#p,q を求めてください。
#
#T個のテストケースが与えられるので、それぞれについて答えを求めてください。
#
#制約
#入力は全て整数
#1≤T≤10
#1≤N≤9×10^18 
#Nは、2 つの相異なる素数 p,q を用いて N=p^2 * qと表せる
#
#入力
#入力は以下の形式で標準入力から与えられる。ここで testiはi番目のテストケースを意味する。
#T
#test1
#test2
#.
#.
#.
#testT
#各テストケースは以下の形式で与えられる。
#N
#
#出力
#T行出力せよ。
#i (1≤i≤T) 行目には、i 番目のテストケースにおける p,q を空白区切りで出力せよ。 なお、この問題の制約下では、N=p^2 * qを満たす素数 p,q の組は 1 通りしか存在しないことが証明できる。
#
#入力例1
#3
#2023
#63
#1059872604593911
#
#出力例1
#17 7
#3 7
#104149 97711

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        p = 0
        q = 0
        for j in range(2, int(N**0.5)+1):
            if N % j == 0:
                p = j
                q = N // j
                break
        print(p, q)

if __name__ == '__main__':
    main()
    