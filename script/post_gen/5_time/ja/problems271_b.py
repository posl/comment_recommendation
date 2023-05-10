Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10**9+7
    n,q = map(int,readline().split())
    a = []
    for _ in range(n):
        a.append(list(map(int,readline().split())))
    for _ in range(q):
        s,t = map(int,readline().split())
        print(a[s-1][t-1])

=======
Suggestion 2

def main():
    n_q = list(map(int, input().split()))
    n = n_q[0]
    q = n_q[1]
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    s_t = []
    for j in range(q):
        s_t.append(list(map(int, input().split())))
    for k in range(q):
        print(a[s_t[k][0]-1][s_t[k][1]-1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 4

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

=======
Suggestion 5

def solve():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 6

def main():
    n,q = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    for i in range(q):
        s,t = map(int, input().split())
        print(a[s-1][t-1])

=======
Suggestion 7

def main():
    import sys
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n,q = map(int,readline().split())
    L = []
    A = []
    for i in range(n):
        l,*a = map(int,readline().split())
        L.append(l)
        A.append(a)
    for i in range(q):
        s,t = map(int,readline().split())
        print(A[s-1][t-1])

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    nums = []
    for i in range(n):
        nums.append(list(map(int, input().split())))

    for i in range(q):
        s, t = map(int, input().split())
        print(nums[s - 1][t - 1])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))

    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t-1])
