def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # print(N, M, K)
    # print(AB)
    # print(CD)
    # 関係を持つ人を記録
    # 1: 友達
    # 2: ブロック
    # 0: その他
    relation = [[0 for _ in range(N)] for _ in range(N)]
    for a, b in AB:
        relation[a-1][b-1] = 1
        relation[b-1][a-1] = 1
    for c, d in CD:
        relation[c-1][d-1] = 2
        relation[d-1][c-1] = 2
    # print(relation)
    # 人ごとに友達候補数をカウント
    ans = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if relation[i][j] == 1:
                ans[i] += 1
                ans[j] += 1
    # print(ans)
    # ブロック関係の人を引く
    for c, d in CD:
        if relation[c-1][d-1] == 2:
            ans[c-1] -= 1
            ans[d-1] -= 1
    # print(ans)
    # 自分自身と友達関係の人を引く
    for i in range(N):
        ans[i] -= relation[i][i]
    # print(ans)
    # 結果を出力
    for a in ans:
        print(a, end=" ")
main()

if __name__ == '__main__':
    main()