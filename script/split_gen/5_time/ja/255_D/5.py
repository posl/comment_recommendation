def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # ここに、問題を解くためのコードを記述する
    # 1 ≦ i ≦ N を満たす整数 i を選択する。
    # 次に、以下の 2 つのうちどちらかを選択し、実行する。
    # A_i に 1 を加算する。
    # A_i から 1 を減算する。
    A.sort()
    A.append(0)
    X.sort()
    ans = 0
    for i in range(N):
        ans += abs(A[i] - A[i+1]) * (i+1)
    ans += A[N] * N
    # print(ans)
    for q in X:
        ans += abs(A[0] - q)
        print(ans)
    # 出力
    # print(ans)
