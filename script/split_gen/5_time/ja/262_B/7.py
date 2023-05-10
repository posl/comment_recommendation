def main():
    N = 0
    M = 0
    U = []
    V = []
    ans = 0
    # 標準入力から N, M, U, V を取得する
    N, M = map(int, input().split())
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    # 頂点 a, b, c を全探索する
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for c in range(1, N + 1):
                # a < b < c かつ、頂点 a と頂点 b を結ぶ辺が存在する。
                # 頂点 b と頂点 c を結ぶ辺が存在する。
                # 頂点 c と頂点 a を結ぶ辺が存在する。
                if a < b < c and (a in U and b in U) and (b in V and c in V) and (c in U and a in V):
                    ans += 1
    # 答えを出力する
    print(ans)
