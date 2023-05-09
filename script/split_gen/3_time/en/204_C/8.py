def main():
    N, M = map(int, input().split())
    # A_i, B_iの入力を受け取る
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 頂点1からの到達可能な頂点を集める
    # 頂点1からの到達可能な頂点の集合を求める
    # 頂点1からの到達可能な頂点の集合
    reachable = set()
    # 頂点1からの到達可能な頂点を集める
    for i in range(M):
        if A[i] == 1:
            reachable.add(B[i])
    # 頂点1からの到達可能な頂点の集合から、さらに到達可能な頂点を集める
    # 頂点1からの到達可能な頂点の集合のサイズ
    size = len(reachable)
    # reachableの要素の数が変わらなくなるまで繰り返す
    while True:
        # reachableの要素の数
        size = len(reachable)
        # 頂点1からの到達可能な頂点の集合から、さらに到達可能な頂点を集める
        for i in range(M):
            if A[i] in reachable:
                reachable.add(B[i])
        # reachableの要素の数が変わらなくなったら、while文を抜ける
        if size == len(reachable):
            break
    # 頂点1からの到達可能な頂点の集合の要素の数
    print(len(reachable))
    return 0
