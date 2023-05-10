Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        tmp = sum([j * A[i + j - 1] for j in range(1, M + 1)])
        if tmp > ans:
            ans = tmp
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            B = A[i:j+1]
            if len(B) == M:
                ans = max(ans, sum([k+1 for k in range(M)]) * sum(B))
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - M + 1):
        B = A[i:i + M]
        sum = 0
        for j in range(M):
            sum += (j + 1) * B[j]
        if sum > ans:
            ans = sum
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    max_sum = 0
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += (j+1)*A[i+j]
        #print(sum)
        if max_sum < sum:
            max_sum = sum
    print(max_sum)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (a[i] * (j + 1)))
            if i + 1 + j + 1 <= n:
                dp[i + 1 + j + 1][j + 1] = max(dp[i + 1 + j + 1][j + 1], dp[i][j])
    print(dp[n][m])

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-M+1):
        ans = max(ans,sum([(i+1)*A[i+j] for j in range(M)]))
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-m+1):
        sum = 0
        for j in range(m):
            sum += (j+1)*a[i+j]
        if sum > ans:
            ans = sum
    print(ans)

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))

    #dp[i][j] := i番目までの要素からj個選んだときの最大値
    dp = [[-float('inf')]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(n):
        for j in range(m+1):
            if j == 0:
                dp[i+1][j] = 0
            else:
                if i >= 1:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][j])
                if i >= 1:
                    dp[i+1][j] = max(dp[i+1][j],dp[i][j-1]+a[i])
    print(max(dp[-1]))

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    #print(N,M,A)

    #Bの部分列を求める
    #Bの長さでループ
    B = []
    for i in range(M,N+1):
        #print("i:",i)
        #Bの開始位置でループ
        for j in range(0,N-i+1):
            #print("j:",j)
            #Bの部分列を作る
            #print(A[j:j+i])
            B.append(A[j:j+i])
    #print(B)

    #Bの部分列の和の最大値を求める
    ans = -10**9
    for b in B:
        #print("b:",b)
        s = 0
        for i in range(1,len(b)+1):
            s += i*b[i-1]
        #print("s:",s)
        ans = max(ans,s)
    print(ans)

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # dp[i][j] := i番目までの要素からj個選んだときのsum_{i=1}^{j} i × B_iの最大値
    # dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + i * A[i - 1])
    dp = [[-float('inf')] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if j > i:
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + i * A[i - 1])

    print(dp[N][M])
