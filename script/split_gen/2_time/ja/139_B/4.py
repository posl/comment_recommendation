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
