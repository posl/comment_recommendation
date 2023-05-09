def solve():
    # 入力
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        P.append(int(p))
        S.append(s)
    # 処理
    # 1. 都市名でソート
    # 2. 都市名が同じなら点数でソート
    # 3. 点数が高い順に出力
    # 4. 都市名が同じなら出現順に出力
    # 5. 都市名が異なるなら出現順に出力
    # 6. 1に戻る
    # 7. 終了
    # 1
    sorted_index = sorted(range(N), key=lambda x: S[x])
    # 2
    sorted_index = sorted(sorted_index, key=lambda x: P[x], reverse=True)
    # 3
    sorted_index = sorted(sorted_index, key=lambda x: S[x])
    # 4
    sorted_index = sorted(sorted_index, key=lambda x: S.index(S[x]))
    # 5
    sorted_index = sorted(sorted_index, key=lambda x: S.index(S[x]))
    # 6
    sorted_index = sorted(sorted_index, key=lambda x: S.index(S[x]))
    # 7
    return sorted_index

if __name__ == '__main__':
    solve()