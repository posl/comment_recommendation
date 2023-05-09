def main():
    N = int(input())
    S = [input() for _ in range(N)]
    # 1. 文字列をソート
    # 2. ソート後の文字列をキーにして、値には文字列のリストを持つ辞書を作成
    # 3. 辞書の値のリストの長さから組み合わせを計算
    # 4. 重複組み合わせを考慮して、組み合わせを計算
    # 5. 組み合わせを出力
    print(sum([len(v) * (len(v) - 1) // 2 for v in sorted([sorted(S)], key=lambda x: x[0])]))
