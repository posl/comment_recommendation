def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # ソートして辞書のキーとして利用する
    # これでアナグラムは同じキーになる
    S = [''.join(sorted(s)) for s in S]
    # 辞書を作成
    # キーがアナグラムの文字列、値がその文字列の数
    D = {}
    for s in S:
        if s in D:
            D[s] += 1
        else:
            D[s] = 1
    # 辞書の値が 2 以上のものの個数をカウント
    cnt = 0
    for v in D.values():
        if v >= 2:
            cnt += v * (v - 1) // 2
    print(cnt)
