def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    # A[i]をMで割った余りを求める
    A = [a % M for a in A]
    # 余りをキーにして、その余りのカードの枚数を値とする辞書を作成する
    d = {}
    for a in A:
        d[a] = d.get(a, 0) + 1
    # 余りが0のカードの枚数を取得する
    n0 = d.get(0, 0)
    # 余りが0でないカードの枚数を取得する
    n1 = N - n0
    # 余りが0でないカードの枚数が0の場合は、答えは0
    if n1 == 0:
        print(0)
        return
    # 余りが0でないカードの枚数が1の場合は、答えは0
    if n1 == 1:
        print(0)
        return
    # 余りが0でないカードの枚数が2以上の場合は、答えはM-1
    # 余りが0でないカードの枚数が2以上の場合は、答えはM-1
    if n1 >= 2:
        print(S - M)
        return
