Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            tmp += (j+1)*A[i+j]
        ans = max(ans,tmp)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(M):
        ans += A[i] * (i+1)
    tmp = ans
    for i in range(N-M):
        tmp -= A[i]
        tmp += A[i+M]
        ans = max(ans, tmp)
    print(ans)

=======
Suggestion 3

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-M+1):
        B = A[i:i+M]
        tmp = 0
        for j in range(len(B)):
            tmp += (j+1)*B[j]
        if tmp > ans:
            ans = tmp
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i, N):
            tmp = 0
            cnt = 1
            for k in range(i, j + 1):
                tmp += cnt * A[k]
                cnt += 1
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-m+1):
        for j in range(m):
            ans+=a[i+j]*(j+1)
    print(ans)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = -10000000000
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            sorted(b)
            tmp = 0
            for k in range(len(b)):
                tmp += (k + 1) * b[k]
            ans = max(ans, tmp)
    print(ans)

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j]+A[i]*(i-j))
            if i+1 < N:
                dp[i+2][j+1] = max(dp[i+2][j+1],dp[i][j]+A[i+1]*(i-j))
    print(dp[N][M])

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    #print(A)
    dp = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i][j] + A[i]*(j+1))
    print(dp[N][M])

=======
Suggestion 9

def solve(n, m, a):
    # dp[i][j] := i番目までの数列からj個選んだ時の最大値
    dp = [[-float('inf')]*(m+1) for _ in range(n+1)]
    dp[0][0] = 0
    for i in range(n):
        for j in range(m+1):
            if j > 0:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j-1] + (i+1)*a[i])
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    return dp[n][m]

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, M, A)
    #print('A[0]:', A[0])
    #print('A[1]:', A[1])
    #print('A[2]:', A[2])
    #print('A[3]:', A[3])
    #print('A[4]:', A[4])
    #print('A[5]:', A[5])
    #print('A[6]:', A[6])
    #print('A[7]:', A[7])
    #print('A[8]:', A[8])
    #print('A[9]:', A[9])
    #print('A[10]:', A[10])
    #print('A[11]:', A[11])
    #print('A[12]:', A[12])
    #print('A[13]:', A[13])
    #print('A[14]:', A[14])
    #print('A[15]:', A[15])
    #print('A[16]:', A[16])
    #print('A[17]:', A[17])
    #print('A[18]:', A[18])
    #print('A[19]:', A[19])
    #print('A[20]:', A[20])
    #print('A[21]:', A[21])
    #print('A[22]:', A[22])
    #print('A[23]:', A[23])
    #print('A[24]:', A[24])
    #print('A[25]:', A[25])
    #print('A[26]:', A[26])
    #print('A[27]:', A[27])
    #print('A[28]:', A[28])
    #print('A[29]:', A[29])
    #print('A[30]:', A[30])
    #print('A[31]:', A[31])
    #print('A[32]:', A[32])
    #print('A[33]:', A[33])
    #print('A[34]:', A[34])
    #print('A[35]:', A[
