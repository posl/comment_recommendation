def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの要素をキーとした辞書を作成
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    # 重複する要素の組み合わせを計算
    ans = 0
    for v in d.values():
        ans += v * (v - 1) // 2
    # 答えを出力
    print(N * (N - 1) // 2 - ans)
