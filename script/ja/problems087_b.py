#問題文
#あなたは、500 円玉を A 枚、100 円玉を B 枚、50 円玉を C 枚持っています。
#これらの硬貨の中から何枚かを選び、合計金額をちょうど X 円にする方法は何通りありますか。
#同じ種類の硬貨どうしは区別できません。2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。
#
#制約
#0 ≦ A, B, C ≦ 50
#A + B + C ≧ 1
#50 ≦ X ≦ 20,000
#A, B, C は整数である
#X は 50 の倍数である
#
#入力
#入力は以下の形式で標準入力から与えられる。
#A
#B
#C
#X
#
#出力
#硬貨を選ぶ方法の個数を出力せよ。
#
#入力例 1
#2
#2
#2
#100
#
#出力例 1
#2
#条件を満たす選び方は以下の 2 通りです。
#500 円玉を 0 枚、100 円玉を 1 枚、50 円玉を 0 枚選ぶ。
#500 円玉を 0 枚、100 円玉を 0 枚、50 円玉を 2 枚選ぶ。
#
#入力例 2
#5
#1
#0
#150
#
#出力例 2
#0
#合計金額をちょうど X 円にする必要があることに注意してください。
#
#入力例 3
#30
#40
#50
#6000
#
#出力例 3
#213

def 