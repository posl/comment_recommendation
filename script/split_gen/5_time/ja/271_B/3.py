def solve():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    queries = [list(map(int, input().split())) for _ in range(Q)]
    # 累積和を作る
    for i in range(N):
        for j in range(1, len(A[i])):
            A[i][j] += A[i][j - 1]
    # クエリ処理
    for query in queries:
        s, t = query
        print(A[s - 1][t - 1])
