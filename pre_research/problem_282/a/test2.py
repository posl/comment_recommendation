#問題文
#整数Kが与えられます。
#英大文字をAから昇順にK個繋げて得られる文字列を答えてください。
#
#制約
#Kは1以上26以下の整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#K
#
#出力
#答えを出力せよ。
#
#入力例1
#3
#
#出力例1
#ABC
#
#入力例2
#1
#
#出力例2
#A

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65 + K)]))

if __name__ == '__main__':
    main()