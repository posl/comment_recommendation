Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    ans = 10 ** 9
    for i in range(1, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                p = s[i]
                q = s[j] - s[i]
                r = s[k] - s[j]
                s_ = s[n] - s[k]
                ans = min(ans, max(p, q, r, s_) - min(p, q, r, s_))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    ans = 10 ** 9
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            ans = min(ans, max(s[i], s[j] - s[i], s[n] - s[j]) - min(s[i], s[j] - s[i], s[n] - s[j]))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_sum = [0] * (N+1)
    for i in range(N):
        A_sum[i+1] = A_sum[i] + A[i]
    #print(A_sum)
    ans = 10**9
    for i in range(1, N-1):
        for j in range(i+1, N):
            P = A_sum[i]
            Q = A_sum[j] - A_sum[i]
            R = A_sum[N] - A_sum[j]
            S = A_sum[N] - A_sum[i]
            #print(P, Q, R, S)
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_cum = [0] * (N + 1)
    for i in range(N):
        A_cum[i + 1] = A_cum[i] + A[i]

    ans = 10 ** 9
    for i in range(3, N - 1):
        #print(i)
        #print(A_cum)
        #print(A_cum[i])
        #print(A_cum[i + 1])
        #print(A_cum[N] - A_cum[i + 1])
        #print(A_cum[N] - A_cum[i])
        #print(A_cum[i + 1] - A_cum[i])
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]) - (A_cum[i - 1] - A_cum[i - 2]))
        #print()
        #print(A_cum[i])
        #print(A_cum[i + 1])
        #print(A_cum[N] - A_cum[i + 1])
        #print(A_cum[N] - A_cum[i])
        #print(A_cum[i + 1] - A_cum[i])
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]))
        #print(A_cum[N] - A_cum[i + 1] - (A_cum[i + 1] - A_cum[i]) - (A_cum[i] - A_cum[i - 1]) - (A_cum[i - 1] - A_cum[i - 2]))
        #print()
        #print(A_cum[i])
        #print(A_cum[i + 1])
        #print

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 累積和を求める
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    # 3箇所で切るので、全ての切り方を試す
    ans = 10**9
    for i in range(1, N-1):
        for j in range(i+1, N):
            # P,Q,R,Sを求める
            P = S[i]
            Q = S[j]-S[i]
            R = S[N]-S[j]
            S_max = max(P, Q, R)
            S_min = min(P, Q, R)
            # 最大値と最小値の差を更新する
            ans = min(ans, S_max-S_min)

    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 前処理
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    # 1つ目の分割
    min_diff = 10 ** 9
    for i in range(1, N - 1):
        P = S[i]
        min_Q = 10 ** 9
        for j in range(i + 1, N):
            Q = S[j] - S[i]
            min_Q = min(min_Q, Q)
            R = S[N] - S[j]
            min_diff = min(min_diff, max(P, Q, R) - min(P, Q, R))
        # 2つ目の分割
        for j in range(i + 1, N):
            Q = S[j] - S[i]
            R = S[N] - S[j]
            min_diff = min(min_diff, max(P, Q, R) - min(P, Q, R))

    print(min_diff)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    #print(S)
    ans = 10 ** 9
    for i in range(N - 3):
        for j in range(i + 1, N - 2):
            for k in range(j + 1, N - 1):
                a = S[i]
                b = S[j] - S[i]
                c = S[k] - S[j]
                d = S[N] - S[k]
                #print(a, b, c, d)
                ans = min(ans, max(a, b, c, d) - min(a, b, c, d))
    print(ans)

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    # 累積和
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])

    # 累積和の最小値
    minS = [0]
    for i in range(N):
        minS.append(min(minS[i], S[i + 1]))

    # 累積和の最大値
    maxS = [0]
    for i in range(N):
        maxS.append(max(maxS[i], S[i + 1]))

    # P,Q,R,S の最大値と最小値の差の絶対値の最小値を求める
    minDiff = 10 ** 9
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            minDiff = min(minDiff, max(maxS[i] - minS[j], maxS[j] - minS[i]) - (S[i] - S[0]))

    print(minDiff)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    if N == 4:
        print(max(A) - min(A))
    else:
        ans = 10**10
        for i in range(3):
            for j in range(i + 1, N - 2):
                for k in range(j + 1, N - 1):
                    P = sum(A[:i + 1])
                    Q = sum(A[i + 1:j + 1])
                    R = sum(A[j + 1:k + 1])
                    S = sum(A[k + 1:])
                    ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
        print(ans)

=======
Suggestion 10

def main():
    import sys
    from itertools import accumulate
    from bisect import bisect_right
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    A = list(accumulate(A))
    res = 10**9
    for i in range(1, N-3):
        #print(A[i])
        j = bisect_right(A, A[i]//2, lo=i+1, hi=N-2)
        #print(j)
        if j <= N-2:
            res = min(res, abs(A[i]-A[j]*2))
        if j-1 >= i+1:
            res = min(res, abs(A[i]-A[j-1]*2))
        k = bisect_right(A, (A[i]+A[N-1])//2, lo=i+1, hi=N-2)
        #print(k)
        if k <= N-2:
            res = min(res, abs(A[N-1]-A[k]*2+A[i]))
        if k-1 >= i+1:
            res = min(res, abs(A[N-1]-A[k-1]*2+A[i]))
    print(res)
