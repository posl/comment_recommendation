Synthesizing 10/10 solutions

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = 10 ** 9
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            if i == j:
                continue
            ans = min(ans, max(S[N] - S[j], S[j] - S[i], S[i] - S[0]) - min(S[N] - S[j], S[j] - S[i], S[i] - S[0]))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    ans = float('inf')
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            x = S[i]
            y = S[j] - S[i]
            z = S[N] - S[j]
            ans = min(ans, max(x, y, z) - min(x, y, z))
    print(ans)

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    c = [0] * n
    d = [0] * n
    e = [0] * n
    b[0] = a[0]
    c[0] = a[0]
    d[n - 1] = a[n - 1]
    e[n - 1] = a[n - 1]
    for i in range(1, n):
        b[i] = b[i - 1] + a[i]
        c[i] = min(b[i], c[i - 1])
        d[n - 1 - i] = d[n - i] + a[n - 1 - i]
        e[n - 1 - i] = min(d[n - 1 - i], e[n - i])
    ans = 10 ** 18
    for i in range(2, n - 1):
        ans = min(ans, max(b[i - 1], e[i + 1]) - min(c[i - 1], d[i + 1]))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = [0]
    for i in range(N):
        s.append(s[-1] + A[i])
    ans = 10 ** 9
    for i in range(1, N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                p = s[i]
                q = s[j] - s[i]
                r = s[k] - s[j]
                s_ = s[-1] - s[k]
                ans = min(ans, max(p, q, r, s_) - min(p, q, r, s_))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A_sum = [0]
    for i in range(N):
        A_sum.append(A_sum[i] + A[i])

    ans = 10**10
    for i in range(1, N-1):
        for j in range(i+1, N):
            P = A_sum[i]
            Q = A_sum[j] - A_sum[i]
            R = A_sum[N] - A_sum[j]
            S = A_sum[N] - A_sum[i]
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))

    print(ans)

=======

def main():
    from bisect import bisect_left
    n = int(input())
    a = list(map(int, input().split()))
    sa = [0] * (n + 1)
    for i in range(n):
        sa[i + 1] = sa[i] + a[i]
    ans = 10**9
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            s1 = sa[i]
            s2 = sa[j] - sa[i]
            s3 = sa[-1] - sa[j]
            ans = min(ans, max(s1, s2, s3) - min(s1, s2, s3))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A

    # 累積和
    cumsum = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        cumsum[i] = cumsum[i-1] + A[i]

    ans = 10**9
    for i in range(2, N-1):
        for j in range(i+1, N):
            P = cumsum[i]
            Q = cumsum[j] - cumsum[i]
            R = cumsum[N] - cumsum[j]
            S = cumsum[N] - cumsum[i]
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
    print(ans)

=======

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A = [0] + A + [0]
    N += 2
    s = [0] * N
    for i in range(N):
        s[i] = s[i-1] + A[i]
    ans = 10**9
    for i in range(2, N-2):
        for j in range(i+1, N-1):
            ans = min(ans, max(s[i], s[j]-s[i], s[N-1]-s[j]) - min(s[i], s[j]-s[i], s[N-1]-s[j]))
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1]-A[0])

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 0 から N-1 までの総和を求める
    S = [0] * (N+1)
    for i in range(N):
        S[i+1] = S[i] + A[i]
    # 総和の最小値と最大値を求める
    minS = min(S)
    maxS = max(S)
    # 総和の最小値と最大値の差の絶対値の最小値を求める
    ans = 10**20
    for i in range(3, N):
        ans = min(ans, max(maxS - S[i], S[i] - minS) - S[i])
    print(ans)
