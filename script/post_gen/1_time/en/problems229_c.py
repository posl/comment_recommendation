Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, W = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    min_a = min(A)
    C = []
    for i in range(N):
        C.append(A[i] - min_a)
    D = []
    for i in range(min_a + 1):
        D.append(0)
    for i in range(N):
        D[C[i]] += B[i]
    for i in range(min_a):
        D[i + 1] += D[i]
    ans = 0
    for i in range(min_a + 1):
        if D[i] <= W:
            ans = max(ans, i * D[i] + D[i])
        else:
            ans = max(ans, i * W + W)
    print(ans)

=======
Suggestion 2

def main():
    N, W = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A, B = zip(*sorted(zip(A, B)))
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, A[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - A[i]] + B[i] * A[i])
    print(dp[W])

=======
Suggestion 3

def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        A, B = map(int, input().split())
        cheese.append((A, B))
    cheese = sorted(cheese, key=lambda x: x[0])
    dp = [0] * (W + 1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j + cheese[i][1] <= W:
                dp[j + cheese[i][1]] = max(dp[j + cheese[i][1]], dp[j] + cheese[i][0] * cheese[i][1])
            dp[j] = max(dp[j], dp[j + cheese[i][1] - W] + cheese[i][0] * (W - j))
    print(max(dp))

=======
Suggestion 4

def main():
    N, W = map(int, input().split())
    cheese = []
    for i in range(N):
        A, B = map(int, input().split())
        cheese.append((A, B))
    cheese.sort()
    dp = [0] * (W+1)
    for i in range(N):
        for j in range(W, -1, -1):
            if j + cheese[i][1] <= W:
                dp[j + cheese[i][1]] = max(dp[j + cheese[i][1]], dp[j] + cheese[i][0] * cheese[i][1])
            dp[j] = max(dp[j], dp[j] + cheese[i][0] * min(W - j, cheese[i][1]))
    print(max(dp))

=======
Suggestion 5

def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        A, B = map(int, input().split())
        cheese.append([A, B])
    cheese.sort(key=lambda x: x[0])
    maxA = cheese[-1][0]
    dp = [0] * (maxA * 1000 + 1)
    for A, B in cheese:
        for i in range(maxA * 1000, A - 1, -1):
            dp[i] = max(dp[i], dp[i - A] + B)
    ans = 0
    for i in range(maxA * 1000 + 1):
        if dp[i] >= W:
            ans = i
            break
    print(ans)

main()

=======
Suggestion 6

def main():
    N, W = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort()
    dp = [0] * (W + 1)
    for a, b in AB:
        for i in range(W, 0, -1):
            if i >= b:
                dp[i] = max(dp[i], dp[i - b] + a * b)
            else:
                dp[i] = max(dp[i], dp[i - 1] + a * i)
    print(dp[W])

=======
Suggestion 7

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0])
    #print(cheese)
    max_cheese = cheese[-1][0]
    #print(max_cheese)
    dp = [0] * (max_cheese + 1)
    for i in range(N):
        for j in range(max_cheese, -1, -1):
            if j + cheese[i][0] > max_cheese:
                continue
            dp[j + cheese[i][0]] = max(dp[j + cheese[i][0]], dp[j] + cheese[i][0] * cheese[i][1])
    #print(dp)
    ans = 0
    for i in range(len(dp)):
        if W >= i:
            ans = max(ans, dp[i] + (W - i) * dp[-1])
    print(ans)

=======
Suggestion 8

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for _ in range(N)]
    cheese.sort(key=lambda x: x[0])
    INF = 10**9+7
    dp = [INF] * (W+1)
    dp[0] = 0
    for a, b in cheese:
        for i in range(W):
            if i+a <= W:
                dp[i+a] = min(dp[i+a], dp[i]+b)
    print(max([a*b for a, b in cheese if b <= dp[W]]))

=======
Suggestion 9

def main():
    N, W = map(int, input().split())
    cheese = [list(map(int, input().split())) for i in range(N)]
    cheese.sort()
    dp = [[0 for i in range(1001)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1001):
            if j < cheese[i-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-cheese[i-1][0]]+cheese[i-1][0]*cheese[i-1][1])
    for i in range(1001):
        if dp[N][i] > W:
            print(i-1)
            return

=======
Suggestion 10

def main():
    import sys
    from collections import defaultdict
    from bisect import bisect_left

    # # for debug
    # f = open("input.txt", "r")
    # sys.stdin = f

    N, W = map(int, input().split())
    cheese = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])

    # 重さをiとしたとき、価値の最大値を記録する
    dp = defaultdict(int)
    # 重さ0のときの価値は0
    dp[0] = 0
    # 重さ1~Wのときの価値を記録する
    for i in range(1, W+1):
        # 重さiに対応する価値の初期値は0
        dp[i] = 0
        # 価値の最大値を探す
        for j in range(N):
            # 重さi以下であれば、価値を計算する
            if cheese[j][0] <= i:
                # 価値が最大値を超えていれば、更新する
                if dp[i] < dp[i-cheese[j][0]] + cheese[j][0] * cheese[j][1]:
                    dp[i] = dp[i-cheese[j][0]] + cheese[j][0] * cheese[j][1]
            # 重さiより大きい場合は、価値は計算する必要がない
            else:
                break
    print(dp[W])
