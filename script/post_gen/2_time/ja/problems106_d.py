Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, Q = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(M)]
    PQ = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, M, Q)
    #print(LR)
    #print(PQ)
    #LRの要素を順に見ていく
    for i in range(Q):
        cnt = 0
        #print(PQ[i])
        for j in range(M):
            #print(LR[j])
            if PQ[i][0] <= LR[j][0] and LR[j][1] <= PQ[i][1]:
                cnt += 1
        print(cnt)

=======
Suggestion 2

def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    train = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        train[L[i]][R[i]] += 1
    for i in range(N + 1):
        for j in range(N + 1):
            if i > 0:
                train[i][j] += train[i - 1][j]
    for i in range(Q):
        ans = 0
        for j in range(p[i], q[i] + 1):
            ans += train[j][q[i]]
        print(ans)

=======
Suggestion 3

def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    p = [0] * Q
    q = [0] * Q
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    for i in range(Q):
        cnt = 0
        for j in range(M):
            if p[i] <= L[j] and R[j] <= q[i]:
                cnt += 1
        print(cnt)

=======
Suggestion 4

def main():
    N, M, Q = map(int, input().split())
    L = [0] * (M + 1)
    R = [0] * (M + 1)
    for i in range(M):
        L[i + 1], R[i + 1] = map(int, input().split())
    p = [0] * (Q + 1)
    q = [0] * (Q + 1)
    for i in range(Q):
        p[i + 1], q[i + 1] = map(int, input().split())
    ans = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            ans[i][j] = ans[i][j - 1] + ans[i - 1][j] - ans[i - 1][j - 1]
            if L[i] <= j <= R[i]:
                ans[i][j] += 1
    for i in range(1, Q + 1):
        print(ans[q[i]][q[i]] - ans[p[i] - 1][q[i]] - ans[q[i]][p[i] - 1] + ans[p[i] - 1][p[i] - 1])

=======
Suggestion 5

def main():
    N, M, Q = map(int, input().split())
    train = [0] * (N + 1)
    for i in range(M):
        L, R = map(int, input().split())
        train[L - 1] += 1
        train[R] -= 1
    for i in range(1, N + 1):
        train[i] += train[i - 1]
    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q] - train[p - 1])

=======
Suggestion 6

def main():
    N, M, Q = map(int, input().split())
    train = [0] * (N + 1)
    for i in range(M):
        L, R = map(int, input().split())
        train[L] += 1
        train[R + 1] -= 1
    for i in range(1, N + 1):
        train[i] += train[i - 1]
    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q] - train[p - 1])

=======
Suggestion 7

def main():
    N, M, Q = map(int, input().split())
    train = [0] * (N+1)
    for i in range(M):
        L, R = map(int, input().split())
        train[L-1] += 1
        train[R] -= 1
    for i in range(N):
        train[i+1] += train[i]
    for i in range(Q):
        p, q = map(int, input().split())
        print(train[q] - train[p-1])

=======
Suggestion 8

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, M, Q = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(M)]
    PQ = [tuple(map(int, input().split())) for _ in range(Q)]
    d = defaultdict(int)
    for l, r in LR:
        d[l] += 1
        d[r+1] -= 1
    for i in range(1, N+1):
        d[i] += d[i-1]
    for p, q in PQ:
        print(d[q]-d[p-1])

main()

=======
Suggestion 9

def main():
    n, m, q = map(int, input().split())

    # 1-indexed
    train = [0] * (n + 1)
    for _ in range(m):
        l, r = map(int, input().split())
        train[l] += 1
        train[r + 1] -= 1

    # 累積和
    for i in range(1, n + 1):
        train[i] += train[i - 1]

    # 累積和
    for i in range(1, n + 1):
        train[i] += train[i - 1]

    for _ in range(q):
        p, q = map(int, input().split())
        print(train[q] - train[p - 1])

=======
Suggestion 10

def main():
    N, M, Q = map(int, input().split())
    # 区間のリストを作成
    interval = []
    for _ in range(M):
        l, r = map(int, input().split())
        interval.append([l, r])
    # 区間のリストをソート
    interval.sort()
    # クエリのリストを作成
    query = []
    for _ in range(Q):
        p, q = map(int, input().split())
        query.append([p, q])
    # クエリのリストをソート
    query.sort(key=lambda x: x[1])
    # クエリのリストを走査
    for p, q in query:
        # 区間のリストを走査
        cnt = 0
        for l, r in interval:
            # 区間のリストの区間が, クエリのリストの区間に含まれているかを判定
            if l <= p and q <= r:
                cnt += 1
        print(cnt)
