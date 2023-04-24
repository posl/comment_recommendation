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
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            ans = min(ans, max(s[i], s[j] - s[i], s[n] - s[j]) - min(s[i], s[j] - s[i], s[n] - s[j]))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*(N+1)
    for i in range(N):
        B[i+1] = B[i] + A[i]
    C = [0]*(N+1)
    for i in range(N):
        C[i+1] = C[i] + A[N-1-i]
    ans = 10**9
    for i in range(1,N-1):
        for j in range(2,N-i+1):
            ans = min(ans, max(B[i],B[i+j],C[N-i],C[N-i-j]) - min(B[i],B[i+j],C[N-i],C[N-i-j]))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    left = [0] * N
    right = [0] * N
    left[0] = A[0]
    right[-1] = A[-1]
    for i in range(1, N):
        left[i] = left[i - 1] + A[i]
        right[-i - 1] = right[-i] + A[-i - 1]
    left_min = min(left)
    left_max = max(left)
    right_min = min(right)
    right_max = max(right)
    ans = min(left_max - left_min, right_max - right_min)
    for i in range(N - 3):
        ans = min(ans, max(left[i], right[i + 1]) - min(left[i], right[i + 1]))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    ans = float('inf')
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            P = S[i]
            Q = S[j] - S[i]
            R = S[N] - S[j]
            ans = min(ans, max(P, Q, R) - min(P, Q, R))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i])
    ans = 10**18
    for i in range(2, N-1):
        L = S[i]
        R = S[N] - S[i]
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < L // 2:
                l = m
            else:
                r = m
        if abs(L - 2 * S[l]) <= abs(L - 2 * S[r]):
            ans = min(ans, max(L - S[l], S[l], R - S[l], S[l]) - min(L - S[l], S[l], R - S[l], S[l]))
        else:
            ans = min(ans, max(L - S[r], S[r], R - S[r], S[r]) - min(L - S[r], S[r], R - S[r], S[r]))
        l = 0
        r = N
        while r - l > 1:
            m = (l + r) // 2
            if S[m] < R // 2:
                l = m
            else:
                r = m
        if abs(R - 2 * S[l]) <= abs(R - 2 * S[r]):
            ans = min(ans, max(L - S[l], S[l], R - S[l], S[l]) - min(L - S[l], S[l], R - S[l], S[l]))
        else:
            ans = min(ans, max(L - S[r], S[r], R - S[r], S[r]) - min(L - S[r], S[r], R - S[r], S[r]))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int,input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])
    ans = 10**18
    for i in range(1,N-1):
        for j in range(i+1,N):
            P = S[i]
            Q = S[j]-S[i]
            R = S[-1]-S[j]
            ans = min(ans,max(P,Q,R)-min(P,Q,R))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    l = [0]
    for a in A:
        l.append(l[-1] + a)
    ans = 10**18
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                ans = min(ans, max(l[i], l[j]-l[i], l[k]-l[j], s-l[k]) - min(l[i], l[j]-l[i], l[k]-l[j], s-l[k]))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    S = [0]
    for i in range(N):
        S.append(S[i]+A[i])
    min_diff = 10**10
    for i in range(1,N-1):
        for j in range(i+1,N):
            min_diff = min(min_diff,abs(S[i]-S[0]-max(S[i]-S[0],S[j]-S[i],S[N]-S[j])))
    print(min_diff)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aの累積和を求める
    cum = [0] * (N + 1)
    for i in range(N):
        cum[i + 1] = cum[i] + A[i]
    # 1つ目の切り口を固定する
    ans = 10 ** 10
    for i in range(1, N - 1):
        # 2つ目の切り口を固定する
        for j in range(i + 1, N):
            # 3つ目の切り口を固定する
            for k in range(j + 1, N):
                # 4つ目の切り口を固定する
                for l in range(k + 1, N):
                    # 4つの累積和の最大値と最小値の差の絶対値を求める
                    ans = min(ans, max(cum[i], cum[j] - cum[i], cum[k] - cum[j], cum[l] - cum[k], cum[N] - cum[l]) - min(cum[i], cum[j] - cum[i], cum[k] - cum[j], cum[l] - cum[k], cum[N] - cum[l]))
    print(ans)

=======
Suggestion 10

def main():
    import sys
    from itertools import accumulate
    readline = sys.stdin.readline
    read = sys.stdin.read

    N, *A = map(int, read().split())
    A = [0] + A
    A = list(accumulate(A))

    ans = 10**9
    for i in range(1, N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                ans = min(ans, max(A[i], A[j]-A[i], A[k]-A[j], A[N]-A[k])-min(A[i], A[j]-A[i], A[k]-A[j], A[N]-A[k]))
    print(ans)
