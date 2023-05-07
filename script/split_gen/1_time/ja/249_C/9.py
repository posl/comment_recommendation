def main():
    import sys
    import re
    from collections import Counter
    from itertools import combinations
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    # 重複を除いた文字列を作成
    S2 = []
    for s in S:
        S2.append("".join(set(s)))
    # 重複しない文字列の組み合わせを作成
    comb = combinations(S2, K)
    # 重複しない文字列の組み合わせの文字数をカウント
    count = []
    for c in comb:
        count.append(len("".join(c)))
    # 最大値を出力
    print(max(count))
