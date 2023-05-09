def main():
    N, L = map(int, input().split())
    # 全てのリンゴの味を求める
    apple_taste = [L + i - 1 for i in range(1, N + 1)]
    # 一番味が悪いリンゴを食べる
    if L <= 0 and 0 <= L + N - 1:
        print(sum(apple_taste))
    # 一番味が悪いリンゴを食べる
    elif L < 0:
        print(sum(apple_taste) - apple_taste[0])
    # 一番味が悪いリンゴを食べる
    elif L + N - 1 < 0:
        print(sum(apple_taste) - apple_taste[-1])
