Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                for l in range(k+1,N):
                    ans = max(ans, P*A[i]+Q*A[j]+R*A[k]+A[l])
    print(ans)

=======
Suggestion 2

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for x in range(N):
        for y in range(x+1, N):
            for z in range(y+1, N):
                for w in range(z+1, N):
                    if A[x] + A[y] + A[z] + A[w] == P + Q + R:
                        ans = 1
    if ans == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N,P,Q,R=map(int,input().split())
    A=list(map(int,input().split()))
    ans=0
    for i in range(N-3):
        for j in range(i+1,N-2):
            for k in range(j+1,N-1):
                for l in range(k+1,N):
                    ans=max(ans,A[i]*P+A[j]*Q+A[k]*R+A[l])
    print(ans)

=======
Suggestion 4

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 'No'
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                for l in range(k+1, N):
                    if A[i] + A[j] + A[k] + A[l] == P + Q + R:
                        ans = 'Yes'
                        break
    print(ans)

=======
Suggestion 5

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-4):
        for j in range(i+1, N-3):
            for k in range(j+1, N-2):
                for l in range(k+1, N-1):
                    ans = max(ans, P*A[i] + Q*A[j] + R*A[k] + A[l])
    print(ans)

=======
Suggestion 6

def solve():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = "No"
    for i in range(N-3):
        for j in range(i+1, N-2):
            for k in range(j+1, N-1):
                for l in range(k+1, N):
                    if A[i]+A[j]+A[k]+A[l] == P+Q+R:
                        ans = "Yes"
    print(ans)

=======
Suggestion 7

def main():
    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [[0] * 4 for _ in range(n)]
    dp[0][0] = a[0] * p
    dp[0][1] = a[0] * q
    dp[0][2] = a[0] * r
    dp[0][3] = 0
    for i in range(1, n):
        dp[i][0] = max(dp[i - 1][0], a[i] * p)
        dp[i][1] = max(dp[i - 1][1], dp[i][0] + a[i] * q)
        dp[i][2] = max(dp[i - 1][2], dp[i][1] + a[i] * r)
        dp[i][3] = max(dp[i - 1][3], dp[i][2])
    print("Yes" if dp[n - 1][3] != 0 else "No")

=======
Suggestion 8

def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))
    #P+Q+Rの最大値を求める
    max_pqr = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                max_pqr = max(max_pqr, P*A[i]+Q*A[j]+R*A[k])
    #P+Q+Rの最大値を満たす(x,y,z,w)を求める
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if P*A[i]+Q*A[j]+R*A[k] == max_pqr:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 9

def main():
    N, P, Q, R = list(map(int, input().split()))
    A = list(map(int, input().split()))

    # 1. 全ての条件を満たす x, y, z, w の組み合わせを列挙する
    # 2. それぞれの組み合わせについて、条件を満たすかどうか判定する
    # 3. どれか一つでも条件を満たす組み合わせがあれば Yes を出力する
    # 4. どれも条件を満たさない組み合わせがあれば No を出力する

    # 1. 全ての条件を満たす x, y, z, w の組み合わせを列挙する
    # x, y, z, w が全て異なる組み合わせを列挙する
    # x, y, z, w が全て異なる組み合わせは、x, y, z, w の組み合わせの数の約数の組み合わせとなる
    # 例えば、x, y, z, w の組み合わせの数が 8 であれば、
    #   (x, y, z, w) = (0, 1, 2, 3)
    #   (x, y, z, w) = (0, 1, 2, 4)
    #   (x, y, z, w) = (0, 1, 2, 5)
    #   (x, y, z, w) = (0, 1, 2, 6)
    #   (x, y, z, w) = (0, 1, 2, 7)
    #   (x, y, z, w) = (0, 1, 3, 4)
    #   (x, y, z, w) = (0, 1, 3, 5)
    #
