Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A_max = max(A)
    A_min = min(A)
    B_max = max(B)
    if A_max < B_max:
        print(0)
        return
    if N == 1:
        print(A[0] * min(B[0], W))
        return
    limit = A_max * W
    dp = [0] * (limit + 1)
    for i in range(N):
        for j in range(limit, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + B[i])
    ans = 0
    for i in range(W + 1):
        ans = max(ans, dp[i])
    print(ans)

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    # 重さが大きい順にソート
    A, B = zip(*sorted(zip(A, B), reverse=True))
    # 累積和をとる
    B = list(accumulate(B))
    # おいしさの最大値を求める
    ans = 0
    for i in range(N):
        # 重さが W を超えたら終了
        if A[i] * B[i] > W:
            break
        # 重さが W 以下のときは、おいしさの最大値を更新
        ans = max(ans, A[i] * B[i])
    # 重さが W を超えたときは、おいしさの最大値を更新
    ans = max(ans, (W - B[i]) * A[i] // B[i])
    print(ans)

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # W 以下の重さのチーズでの最大値を求める
    # 重さの総和は W 以下なので、重さの最大値は W とする
    dp = [0] * (W + 1)

    # チーズの重さの総和は 1 から W まで試す
    for i in range(1, W + 1):
        # チーズの種類を 1 から N まで試す
        for j in range(N):
            # チーズの重さが i 以下のとき
            if i - B[j] >= 0:
                # 今までの最大値と、今回のチーズを使ったときの最大値を比べる
                dp[i] = max(dp[i], dp[i - B[j]] + A[j])

    print(dp[W])

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(N):
        if W < cheese[i][1]:
            ans += cheese[i][0] * W / cheese[i][1]
            break
        else:
            ans += cheese[i][0]
            W -= cheese[i][1]
    print(int(ans))

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(N):
        if W >= cheese[i][1]:
            ans += cheese[i][0]
            W -= cheese[i][1]
        else:
            ans += cheese[i][0] * W / cheese[i][1]
            break
    print(int(ans))

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        cheese.append(list(map(int, input().split())))
    cheese = sorted(cheese, key=lambda x: x[0] / x[1])
    ans = 0
    for i in range(N):
        if cheese[i][1] <= W:
            ans += cheese[i][0]
            W -= cheese[i][1]
        else:
            ans += cheese[i][0] * W / cheese[i][1]
            break
    print(int(ans))

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    cheese = [tuple(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1], reverse=True)
    ans = 0
    for i in range(N):
        if W > 0:
            if cheese[i][1] <= W:
                ans += cheese[i][0]
                W -= cheese[i][1]
            else:
                ans += cheese[i][0] * W / cheese[i][1]
                W = 0
    print(int(ans))

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0]/x[1])
    dp = [0]*(W+1)
    for a, b in cheese:
        for i in range(W, -1, -1):
            if i+b <= W:
                dp[i+b] = max(dp[i+b], dp[i]+a)
    print(max(dp))

=======
Suggestion 9

def main():
    n, w = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(n)]
    cheese.sort(key=lambda x: x[0]/x[1])
    ans = 0
    for i in range(n):
        if cheese[i][1] <= w:
            ans += cheese[i][0]
            w -= cheese[i][1]
        else:
            ans += cheese[i][0] * w / cheese[i][1]
            break
    print(int(ans))

=======
Suggestion 10

def read_int():
    return int(input())
