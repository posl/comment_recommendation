def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # 1. Aの最大値を求める
    # 2. Xの最大値を求める
    # 3. Aの最大値とXの最大値の大きい方の値を求める
    # 4. 3で求めた値をQ回かける
    # 5. 4で求めた値を出力する
    max_a = max(A)
    max_x = max(X)
    max_ax = max(max_a, max_x)
    ans = max_ax * Q
    print(ans)
