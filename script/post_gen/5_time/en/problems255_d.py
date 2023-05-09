Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    ans = []
    for i in range(q):
        x_i = x[i]
        ans.append(sum([abs(a_j-x_i) for a_j in a]))
    print(sum(ans))

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    a.sort()
    s = sum(a)
    for i in range(q):
        print(n*x[i]+s)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    X.sort()
    ans = 0
    for i in range(Q):
        ans += abs(A[0] - X[i])
    print(ans)

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    A.sort()
    A.append(10**9+1)
    X.append(0)

    ans = 0
    for i in range(N):
        ans += abs(A[i] - A[i+1])

    for x in X:
        for i in range(N):
            if A[i] <= x <= A[i+1]:
                ans -= abs(A[i] - x)
                ans += abs(A[i+1] - x)
                break
        print(ans)

=======
Suggestion 5

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    A.sort()
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    for x in X:
        l = -1
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if A[m] >= x:
                r = m
            else:
                l = m
        ans = 0
        if r > 0:
            ans += x * r - s[r]
        if r < N:
            ans += s[N] - s[r] - x * (N - r)
        print(ans)

=======
Suggestion 6

def main():
    n, q = list(map(int, input().split()))
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]

    max_a = max(a)
    min_a = min(a)
    max_x = max(x)
    min_x = min(x)

    max_value = max(max_a, max_x)
    min_value = min(min_a, min_x)

    if max_value == min_value:
        print(0)
        return

    a = [ai - min_value for ai in a]
    x = [xi - min_value for xi in x]

    n = max_value - min_value + 1

    d = [0] * n
    for i in range(n - 1):
        d[i + 1] = d[i] + a[i]

    for xi in x:
        if xi == 0:
            print(0)
            continue

        ans = 0
        for i in range(n - 1):
            if d[i] <= xi < d[i + 1]:
                ans += xi * (i + 1) - d[i]
                ans += d[-1] - d[i + 1] - xi * (n - i - 1)
                break
            else:
                ans += d[i + 1] - d[i]

        print(ans)

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for i in range(Q)]

    A.sort()
    A.append(0)
    A.append(10**9+1)
    A.sort()
    A = [A[i+1]-A[i] for i in range(N+1)]
    A.sort()
    A = [A[i+1]-A[i] for i in range(N)]
    #print(A)
    #print(X)

    s = sum(A)
    for x in X:
        print(s-x)

=======
Suggestion 8

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]
    # A = [6, 11, 2, 5, 5]
    # X = [5, 20, 0]
    # N, Q = 5, 3
    # A = [1000000000, 314159265, 271828182, 141421356, 161803398, 0, 777777777, 255255255, 536870912, 998244353]
    # X = [555555555, 321654987, 1000000000, 789456123, 0]

    A.sort()
    # print(A)
    # print(X)
    s = sum(A)
    # print(s)

    for i in range(Q):
        x = X[i]
        # print(x)
        # print(A)
        # print(s)
        # print()
        j = 0
        while j < N and A[j] < x:
            j += 1
        # print(j)
        if j == N:
            print(s + (x - A[-1]))
        else:
            print(s - (N - j) * (x - A[j]))

=======
Suggestion 9

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = [int(input()) for _ in range(Q)]

    # Aをソートする
    A.sort()

    # Aの累積和を計算する
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # Aの累積和の最大値
    M = S[N]

    # 各クエリに答える
    for x in X:
        # x以下の要素の個数を二分探索で求める
        ok = 0
        ng = N + 1
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if A[mid - 1] <= x:
                ok = mid
            else:
                ng = mid

        # x以下の要素の個数を求める
        k = ok

        # x以下の要素の総和を求める
        s = S[k]

        # xより大きい要素の個数を求める
        m = N - k

        # x以下の要素の総和をxに変えるのに必要な操作回数を求める
        ans = s - k * x

        # xより大きい要素の総和をxに変えるのに必要な操作回数を求める
        ans += (M - s) - m * (x + 1)

        # 出力する
        print(ans)

=======
Suggestion 10

def process():
    pass
