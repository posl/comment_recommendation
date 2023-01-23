#問題文
#英小文字、(、) からなる文字列のうち、以下の手順によって空文字列になるものを良い文字列と呼びます:
#
#まず、英小文字をすべて削除する。
#次に、連続する () が存在する限り、それを削除する。
#例えば、((a)ba) は英小文字をすべて削除すると (()) となり、2文字目と3文字目に連続する () を削除すると () となり、最終的に空文字列にすることができるので良い文字列です。
#
#良い文字列 S が与えられます。 S の i 文字目を Siで表します。
#各英小文字 a , b , … , z に対して、その文字が書かれたボールが 1 つあります。 また、空の箱があります。
#高橋君は i=1,2, … ,∣S∣ に対してこの順に気を失わない限り操作を行います。
#Siが英小文字ならば、その英小文字が書かれたボールを箱に入れる。ただし、そのボールがすでに箱に入っている場合、高橋君は気を失う。
#Siが ( ならば、何もしない。
#Siが ) ならば、i 未満の整数 j であって、S の j 番目から i 番目までの文字からなる文字列が良い文字列となる最大の整数 j を取る。
#（このような整数 j は必ず存在することが証明できる。）j 番目から i 番目までの操作で箱に入れたボールをすべて、箱から取り出す。
#高橋君が気を失わずに一連の操作を完了させられるか判定してください。
#
#制約
#1≤∣S∣≤3×10^5
#Sは良い文字列
#
#
#入力
#入力は以下の形式で標準入力から与えられる。
#S
#
#出力
#高橋君が気を失わずに一連の操作を完了させられるならば Yes を、そうでないならば No を出力せよ。
#
#入力例1
#((a)ba)
#
#出力例1
#Yes
#
#入力例2
#(a(ba))
#
#出力例2
#No
#
#入力例3
#(((())))
#
#出力例3
#Yes
#
#入力例4
#abca
#
#出力例4
#No

def main():
    s = input()
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                print('No')
                return
            stack.pop()
        else:
            if len(stack) > 0:
                print('No')
                return
    if len(stack) == 0:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()