def prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
a, b, c, d = map(int, input().split())
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if prime(i + j):
            print("Aoki")
            exit()
print("Takahashi")
問題文
高橋君と青木君が次のようなゲームをします。
まず、高橋君が A 以上 B 以下の好きな整数を選び、青木君に伝える
次に、青木君が C 以上 D 以下の好きな整数を選ぶ
二人の選んだ整数の和が素数なら青木君の勝ち、そうでなければ高橋君の勝ち
二人が最適な戦略を取るとき、どちらが勝ちますか？
制約
1 ≦ A ≦ B ≦ 100
1 ≦ C ≦ D ≦ 100
入力に含まれる値は全て整数である
入力
入力は以下の形式で標準入力から与えられる。
A B C D
出力
二人が最適な戦略をとったとき、高橋君が勝つなら Takahashi、青木君が勝つなら Aoki を出力せよ。
入力例 1
2 3 3 4
出力例 1
Aoki
例えば高橋君が 2 を選んだときは、青木君は 3 を選ぶことで、和を素数であ

if __name__ == '__main__':
    prime()