def main():
    N, M, Q = map(int, input().split())
    # 荷物の大きさと価値
    W = [0] * N
    V = [0] * N
    for i in range(N):
        W[i], V[i] = map(int, input().split())
    # 箱の大きさ
    X = [0] * M
    for i in range(M):
        X[i] = int(input())
    # クエリ
    Query = [[0] * 2 for _ in range(Q)]
    for i in range(Q):
        Query[i][0], Query[i][1] = map(int, input().split())
    for i in range(Q):
        # 箱の大きさのリスト
        X_list = [0] * (M + 1)
        for j in range(M):
            X_list[j] = X[j]
        # 箱の大きさをソート
        X_list.sort()
        # 箱の大きさのリストの中で使えない箱の大きさを0にする
        for j in range(Query[i][0] - 1, Query[i][1]):
            X_list[j] = 0
        # 箱の大きさのリストの中で使えない箱の大きさを削除
        X_list = list(filter(lambda x: x != 0, X_list))
        # 荷物の大きさと価値のリスト
        WV_list = [[0, 0]] * N
        for j in range(N):
            WV_list[j][0] = W[j]
            WV_list[j][1] = V[j]
        # 荷物の大きさと価値のリストをソート
        WV_list.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for j in range(N):
            for k in range(len(X_list)):
                if WV_list[j][0] <= X_list[k]:
                    ans += WV_list[j][1]
                    X_list[k] = 0
                    break
        print(ans)
