def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    # おいしさの大きい順にソート
    sushi.sort(key=lambda x: x[1], reverse=True)
    # おいしさの大きい順に K 個の寿司を食べる
    # そのときの種類数を求める
    kind = set()
    satis = 0
    for i in range(K):
        satis += sushi[i][1]
        kind.add(sushi[i][0])
    # 種類数の種類数を求める
    kind_num = len(kind)
    # おいしさの大きい順に K 個の寿司を食べたときの種類数の種類数の最大値を求める
    # おいしさの小さい順に食べていく
    for i in range(K):
        # おいしさの大きい順に K 個の寿司を食べたときの種類数の種類数を更新
        if sushi[i][0] in kind:
            kind_num -= 1
            kind.remove(sushi[i][0])
        # おいしさの小さい順に食べていく
        for j in range(K, N):
            # おいしさの小さい順に食べていく寿司が種類数に含まれていない場合
            if sushi[j][0] not in kind:
                # おいしさの大きい順に K 個の寿司を食べたときの種類数の種類数を更新
                kind_num += 1
                kind.add(sushi[j][0])
                # おいしさの大きい順に K 個の寿司を食べたときの種

if __name__ == '__main__':
    main()