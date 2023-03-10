#問題文
#整数 A,B が与えられます。 A^Bの値を出力してください。
#
#制約
#1≤A,B≤9
#入力はすべて整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A B
#
#出力
#答えを出力せよ。
#
#入力例1
#4 3
#
#出力例1
#64
#
#入力例2
#5 5
#
#出力例2
#3125
#
#入力例3
#8 1
#
#出力例3
#8

def main():
    A, B = map(int, input().split())
    print(A ** B)

if __name__ == '__main__':
    main()