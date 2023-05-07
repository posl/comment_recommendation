def main():
    # 標準入力から整数値を取得する
    n = int(input())
    # 標準入力から整数値を取得してリストに格納する
    l = list(map(int, input().split()))
    # 結果を格納する変数
    r = 0
    # 三角形を作ることのできるような長さの異なる 3 本の棒を選ぶ方法を全て調べる
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # 三角形の成立条件を満たすかどうか調べる
                if l[i] != l[j] and l[j] != l[k] and l[k] != l[i] and l[i] + l[j] > l[k] and l[j] + l[k] > l[i] and l[k] + l[i] > l[j]:
                    # 三角形の成立条件を満たす場合は結果に 1 を加算する
                    r += 1
    # 結果を出力する
    print(r)

if __name__ == '__main__':
    main()