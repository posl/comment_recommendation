def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    # 種類ごとの食べた回数を保存する配列
    kinds = [0] * (N + 1)
    # 食べた回数の最大値を保存する変数
    kinds_max = 0
    # 今回食べた種類の数を保存する変数
    kinds_cnt = 0
    # 種類ごとの食べた回数を保存する配列
    kinds = [0] * (N + 1)
    # 種類ごとに食べた回数を記録する
    for i in range(K):
        kinds[sushi[i][0]] += 1
        # 種類が増えたらカウント
        if kinds[sushi[i][0]] == 1:
            kinds_cnt += 1
    # 最大値を更新
    kinds_max = max(kinds_max, kinds_cnt)
    # 今回食べた種類の数を保存する変数
    kinds_cnt = 0
    # 種類ごとの食べた回数を保存する配列
    kinds = [0] * (N + 1)
    # 一番美味しいものを食べる
    kinds[sushi[0][0]] += 1
    kinds_cnt += 1
    # 一番美味しいもの以外を食べる
    for i in range(1, K):
        kinds[sushi[i][0]] += 1
        # 種類が増えたらカウント
        if kinds[sushi[i][0]] == 1:
            kinds_cnt += 1
        # 一番美味しいものと同じ種類のものを食べる
        if sushi[i][0] == sushi

if __name__ == '__main__':
    main()