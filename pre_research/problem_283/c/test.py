#問題文
#高橋君は、レジ打ちの仕事をしています。
#レジの機械には 00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 の11個のボタンがあります。 レジの機械には、はじめ0が表示されています。 ボタン00を押すと、表示されている数が100倍されます。 
#それ以外のボタンを押すと、表示されている数が10倍されたあとに、押されたボタンに書かれている数が加算されます。
#高橋君は、レジに整数Sを表示させたいです。 レジにSが表示されている状態にするためには、少なくとも何回ボタンを押す必要があるか求めてください。
#
#制約
#1≤S≤10 
#100000 
#S は整数
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#答えを1行で出力せよ。
#
#入力例1
#40004
#
#出力例1
#4
#
#入力例2
#1355506027
#
#出力例2
#10
#
#入力例3
#10888869450418352160768000001
#
#出力例３
#27

def main():
    S = input()
    print(len(S))

if __name__ == '__main__':
    main()