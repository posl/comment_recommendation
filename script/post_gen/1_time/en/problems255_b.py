Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    left = 0
    right = 10 ** 10
    for _ in range(100):
        mid = (left + right) / 2
        ok = False
        for i in range(N):
            if i + 1 in A:
                continue
            for j in range(i + 1, N):
                if j + 1 in A:
                    continue
                if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 <= mid ** 2:
                    ok = True
        if ok:
            right = mid
        else:
            left = mid
    print(left)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0]*N
    Y = [0]*N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    l = 0
    r = 10**10
    while r-l > 10**(-5):
        m = (l+r)/2
        if check(N, K, A, X, Y, m):
            r = m
        else:
            l = m
    print(r)

=======
Suggestion 3

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

=======
Suggestion 4

def main():
    import math
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            ans = max(ans, math.sqrt((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2))
    for i in range(K - 1):
        ans = max(ans, math.sqrt((X[A[i] - 1] - X[A[i + 1] - 1]) ** 2 + (Y[A[i] - 1] - Y[A[i + 1] - 1]) ** 2))
    print(ans / 2)

=======
Suggestion 5

def distance(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

=======
Suggestion 6

def main():
    import sys
    import math
    input = sys.stdin.readline

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())

    def is_ok(R):
        # 人iが光iに照らされるかどうか
        is_lit = [False] * N
        for i in range(K):
            is_lit[A[i]-1] = True

        # 光iが人jに照らすかどうか
        is_light = [[False] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if (X[i]-X[j])**2 + (Y[i]-Y[j])**2 <= R**2:
                    is_light[i][j] = True

        # 光iが人jに照らすかどうかでグループ化
        group = [0] * N
        group_num = 0
        for i in range(N):
            if is_lit[i]:
                group[i] = group_num
                group_num += 1
            else:
                for j in range(i):
                    if is_light[j][i]:
                        group[i] = group[j]
                        break

        # 人iが光iに照らされるかどうか
        for i in range(N):
            for j in range(N):
                if group[i] == group[j]:
                    is_lit[j] = is_lit[j] or is_light[i][j]

        return all(is_lit)

    # 二分探索
    ng = 0
    ok = 2*10**5
    while abs(ok-ng) > 10**-5:
        mid = (ok+ng)/2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

=======
Suggestion 7

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)

=======
Suggestion 8

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

=======
Suggestion 9

def solve(n, k, a, x, y):
    def ok(r):
        seen = [False] * n
        for i in range(k):
            seen[a[i] - 1] = True
        for i in range(n):
            if seen[i]:
                continue
            for j in range(k):
                if ((x[i] - x[a[j] - 1]) ** 2 + (y[i] - y[a[j] - 1]) ** 2) ** 0.5 <= r:
                    seen[i] = True
                    break
        return all(seen)
    ng = -1
    ok = 10 ** 10
    while abs(ok - ng) > 10 ** -5:
        mid = (ok + ng) / 2
        if ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

=======
Suggestion 10

def main():
    import sys
    from math import sqrt

    def input(): return sys.stdin.readline().rstrip()

    def dist(x1, y1, x2, y2):
        return sqrt((x1-x2)**2 + (y1-y2)**2)

    def check(x, y, r, n, k, a, X, Y):
        for i in range(n):
            if i+1 in a:
                if dist(x, y, X[i], Y[i]) > r:
                    return False
            else:
                if dist(x, y, X[i], Y[i]) <= r:
                    return False
        return True

    def solve(n, k, a, X, Y):
        ans = 10**10
        for i in range(n):
            for j in range(i+1, n):
                x = (X[i] + X[j]) / 2
                y = (Y[i] + Y[j]) / 2
                r = dist(x, y, X[i], Y[i])
                if check(x, y, r, n, k, a, X, Y):
                    ans = min(ans, r)
                for l in range(j+1, n):
                    x = (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j])) / \
                        (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j]))
                    y = (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j])) / \
                        (X[i]*(Y[j]-Y[l]) + X[j]*(Y[l]-Y[i]) + X[l]*(Y[i]-Y[j]))
                    r = dist(x, y, X[i], Y[i])
                    if check(x, y, r, n, k, a, X, Y):
                        ans = min(ans, r)
        return ans

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    X = []
    Y = []
    for i in range(n):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    print(solve
