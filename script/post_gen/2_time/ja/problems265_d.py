Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    if A[i]+A[j]+A[k]+A[l] == P+Q+R:
                        ans = "Yes"
    print(ans)

=======
Suggestion 2

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                if P == sum(A[i:j]) and Q == sum(A[j:k]) and R == sum(A[k:]):
                    ans = "Yes"
    print(ans)

=======
Suggestion 3

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    if A[i]+A[j]+A[k] == P and A[j]+A[k]+A[l] == Q and A[k]+A[l] == R:
                        ans = "Yes"
                        break
    print(ans)

=======
Suggestion 4

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "No"
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if P * A[i] + Q * A[j] + R * A[k] == P * A[i] + Q * A[j] + R * A[k]:
                    ans = "Yes"
    print(ans)

=======
Suggestion 5

def main():
    N,P,Q,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = "No"
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if A[i]*P + A[j]*Q + A[k]*R == 0:
                    ans = "Yes"
                    break
    print(ans)

=======
Suggestion 6

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * 4 for _ in range(n + 1)]
    for i in range(n):
        dp[i + 1][0] = max(dp[i][0], a[i])
        dp[i + 1][1] = max(dp[i][1], dp[i + 1][0] + a[i])
        dp[i + 1][2] = max(dp[i][2], dp[i + 1][1] + a[i])
        dp[i + 1][3] = max(dp[i][3], dp[i + 1][2] + a[i])
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][0] * p + dp[i][1] * q + dp[i][2] * r + dp[i][3])
    print(ans)

=======
Suggestion 7

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = "No"
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if a[i] * p + a[j] * q + a[k] * r == p + q + r:
                    ans = "Yes"
                    break
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    #P,Q,Rの最大値を求める
    maxP = 0
    maxQ = 0
    maxR = 0
    for i in range(N):
        maxP = max(maxP, S[i + 1] - S[0])
        maxQ = max(maxQ, S[i + 1] - S[max(0, i - P + 1)])
        maxR = max(maxR, S[i + 1] - S[max(0, i - Q + 1)])
    #条件を満たす組が存在するか判定
    for i in range(N):
        if (S[i + 1] - S[max(0, i - R + 1)]) == maxR:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def main():
    n,p,q,r = map(int,input().split())
    a = list(map(int,input().split()))
    #累積和を求める
    sum_a = [0]*(n+1)
    for i in range(n):
        sum_a[i+1] = sum_a[i] + a[i]
    #P,Q,Rの最大値を求める
    max_p = max_q = max_r = 0
    for i in range(n):
        max_p = max(max_p, sum_a[i+1]-sum_a[0])
        max_q = max(max_q, sum_a[i+1]-sum_a[max(0,i-p+1)])
        max_r = max(max_r, sum_a[i+1]-sum_a[max(0,i-q+1)])
    #P,Q,Rの最大値になる組を求める
    max_pq = max_pr = max_qr = 0
    for i in range(n):
        max_pq = max(max_pq, sum_a[i+1]-sum_a[max(0,i-p+1)]+max_q)
        max_pr = max(max_pr, sum_a[i+1]-sum_a[max(0,i-q+1)]+max_r)
        max_qr = max(max_qr, sum_a[i+1]-sum_a[max(0,i-r+1)]+max_p)
    #P,Q,Rの最大値になる組が条件を満たすか判定する
    if max_p+max_q+max_r < max_pq+max_pr+max_qr:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    # a[0]を使う場合の最大値
    dp0 = [0] * n
    dp0[0] = a[0] * p
    for i in range(1, n):
        dp0[i] = max(dp0[i - 1], a[i] * p)
    # a[0]とa[1]を使う場合の最大値
    dp1 = [0] * n
    dp1[1] = dp0[0] + a[1] * q
    for i in range(2, n):
        dp1[i] = max(dp1[i - 1], dp0[i - 1] + a[i] * q)
    # a[0]とa[1]とa[2]を使う場合の最大値
    dp2 = [0] * n
    dp2[2] = dp1[1] + a[2] * r
    for i in range(3, n):
        dp2[i] = max(dp2[i - 1], dp1[i - 1] + a[i] * r)
    # a[0]とa[1]とa[2]とa[3]を使う場合の最大値
    dp3 = [0] * n
    dp3[3] = dp2[2]
    for i in range(4, n):
        dp3[i] = max(dp3[i - 1], dp2[i - 1])
    # a[0]とa[1]とa[2]とa[3]とa[4]を使う場合の最大値
    dp4 = [0] * n
    dp4[4] = dp3[3]
    for i in range(5, n):
        dp4[i] = max(dp4[i - 1], dp3[i - 1])
    # a[0]とa[1]とa[2]とa[3]とa[4]とa[5]を使う場合の最大
