def main():
    # 1行目の入力
    n, l = map(int, input().split())
    # リストの初期化
    apple = []
    # リストの作成
    for i in range(n):
        apple.append(l+i)
    # 最適なリンゴを食べる
    apple.remove(min(apple, key=lambda x: abs(x)))
    # リンゴの味の合計を求める
    print(sum(apple))
