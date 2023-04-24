Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print((B + A - 3) // (A - 1))

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print((B - 1 + A - 2) // (A - 1))

=======
Suggestion 5

def main():
    A,B = map(int,input().split())
    if B%A == 0:
        print(B//A)
    else:
        print(B//A+1)
main()

問題文

高橋くんの家には電源プラグの差込口が 1 口しかありません。
そこで、高橋くんは A 個口の電源タップをいくつか使って未使用の差込口を B 口以上に拡張したいと考えています。
A 個口の電源タップ 1 つと未使用の差込口 1 口を使って、新たに差込口を A 口増やすことができます。
最小でいくつの電源タップが必要でしょうか。

制約

入力は全て整数である。

2 ≦ A ≦ 20

1 ≦ B ≦ 20

入力

入力は以下の形式で標準入力から与えられる。

A B

出力

必要な電源タップの個数の最小値を出力せよ。

入力例 1

4 10

出力例 1

3

4 個口の電源タップを 3 つ使うと、未使用の差込口は 10 口になります。

入力例 2

8 9

出力例 2

2

8 個口の電源タップを 2 つ使うと、未使用の差込口は 15 口になります。

入力例 3

8 8

出力例 3

1

問題文

高橋くんは電源タップを 1 つ持っています。
高橋くんは電源タップを 1 つ使って、未使用の差込口を 1 口以上に拡張した

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    print((b-1)//(a-1))

=======
Suggestion 7

def main():
    # 標準入力からAとBを取得
    A, B = map(int, input().split())

    # AをBで割った余りを取得
    remainder = B % A
    # 余りが0でない場合は、余りをAに加算して、商に1を足す
    if remainder != 0:
        A += remainder
        B = B // A + 1
    # 余りが0の場合は、商に1を足す
    else:
        B = B // A

    # 商を出力
    print(B)
