Synthesizing 10/10 solutions

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 10 ** 20
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            p = s[i]
            q = s[j] - s[i]
            r = s[n] - s[j]
            ans = min(ans, max(p, q, r) - min(p, q, r))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))

    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + A[i - 1]

    ans = float('inf')
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            P = S[i]
            Q = S[j] - S[i]
            R = S[N] - S[j]
            S_max = max(P, Q, R)
            S_min = min(P, Q, R)
            ans = min(ans, S_max - S_min)
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    for i in range(1, N + 1):
        A[i] += A[i - 1]
    ans = 10 ** 9
    for i in range(2, N - 1):
        ans = min(ans, max(A[i - 1], A[N] - A[i - 1], A[N] - A[i]) - min(A[i - 1], A[N] - A[i - 1], A[N] - A[i]))
    print(ans)

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(1, n+1):
        a[i] += a[i-1]
    ans = 10**9
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                b = a[i]
                c = a[j] - a[i]
                d = a[k] - a[j]
                e = a[n] - a[k]
                ans = min(ans, max(b, c, d, e) - min(b, c, d, e))
    print(ans)

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # a = [3, 2, 4, 1, 2]
    # a = [10, 71, 84, 33, 6, 47, 23, 25, 52, 64]
    # a = [1, 2, 3, 1000000000, 4, 5, 6]
    # a = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # a = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # a = [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    # a = [14, 13, 12

=======

def main():
    import sys
    from itertools import accumulate
    from bisect import bisect_left
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A_acc = [0] + list(accumulate(A))
    A_acc_rev = [0] + list(accumulate(reversed(A)))
    A_acc_rev = list(reversed(A_acc_rev))
    ans = 10**9
    for i in range(2, N-1):
        P = A_acc[i]
        Q = A_acc[N] - A_acc[i]
        R = bisect_left(A_acc, (A_acc[i] + A_acc[N]) // 2)
        if R == N:
            R = N - 1
        S = bisect_left(A_acc_rev, (A_acc[i] + A_acc[N]) // 2)
        if S == N:
            S = N - 1
        ans = min(ans, max(P, Q, A_acc[R], A_acc[N] - A_acc[R]) - min(P, Q, A_acc[R], A_acc[N] - A_acc[R]))
        ans = min(ans, max(P, Q, A_acc_rev[S], A_acc_rev[N] - A_acc_rev[S]) - min(P, Q, A_acc_rev[S], A_acc_rev[N] - A_acc_rev[S]))
    print(ans)

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sum_a = sum(a)
    sum_l = 0
    sum_r = sum_a
    min_diff = 10**9
    for i in range(n - 1):
        sum_l += a[i]
        sum_r -= a[i]
        diff = abs(sum_l - sum_r)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**18
    for i in range(2):
        A1 = A[:i+1]
        A2 = A[i+1:]
        for j in range(2):
            B1 = A1[:j+1]
            B2 = A1[j+1:]
            for k in range(2):
                C1 = A2[:k+1]
                C2 = A2[k+1:]
                ans = min(ans, max(sum(B1), sum(B2), sum(C1), sum(C2)) - min(sum(B1), sum(B2), sum(C1), sum(C2)))
    print(ans)
solve()

=======

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    Ans = float("inf")
    for i in range(4):
        for j in range(4):
            if i + j > N - 4:
                break
            if i + j > 0:
                Ans = min(Ans, A[i + j + N - 4] - A[i])
    print(Ans)

=======

def main():
    N = int(input())
    A = list(map(int,input().split()))

    S = sum(A)
    S1 = S
    S2 = S
    S3 = S

    ans = 10**18
    for i in range(N-1):
        S1 -= A[i]
        S2 -= A[i]
        S3 -= A[i]
        if i > 0:
            S2 -= A[i-1]
            S3 -= A[i-1]
        if i > 1:
            S3 -= A[i-2]
        if i < N-2:
            S2 += A[i+1]
            S3 += A[i+1]
        if i < N-3:
            S3 += A[i+2]

        ans = min(ans, max(S1,S2,S3) - min(S1,S2,S3))
    print(ans)

main()
