def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 1. Aの要素の符号を反転させる
    # 2. 1で反転させた要素のうち、最も絶対値の大きいものを求める
    # 3. 2で求めた要素の絶対値を加算する
    # 1
    A = [-a if i % 2 == 1 else a for i, a in enumerate(A)]
    # 2
    max_a = max(A)
    # 3
    print(sum(A) - max_a)
