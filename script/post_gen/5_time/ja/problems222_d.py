Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mod = 998244353
    dp = [[0 for i in range(3001)] for j in range(3001)]

    dp[0][0] = 1
    for i in range(n):
        for j in range(a[i], b[i]+1):
            dp[i+1][j] = dp[i+1][j-1] + dp[i][j]
            dp[i+1][j] %= mod
        for j in range(b[i]+1, 3001):
            dp[i+1][j] = dp[i+1][j-1]
    print(dp[n][3000])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = 1
    for i in range(N):
        ans *= (min(B[i], max(A[i], B[i - 1])) - A[i] + 1)
        ans %= 998244353
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[i][j] = i番目までの要素を使って、j番目の数値を作ることが出来る通り数
    dp = [[0] * 3001 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(3001):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= 998244353
            if A[i] <= j and j <= B[i]:
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= 998244353
    print(dp[N][B[N - 1]])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 998244353

    # dp[i][j] := i番目まで見たときに、jが最後になるような数列の数
    dp = [[0] * 3010 for _ in range(3010)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= mod

    print(sum(dp[N]) % mod)

=======
Suggestion 5

def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    ans = 1
    for i in range(n):
        ans *= max(0, b[i] + 1 - a[i])
        ans %= 998244353
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    MOD = 998244353

    dp = [[0 for _ in range(3001)] for _ in range(3001)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(A[i], B[i] + 1):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            dp[i + 1][j] += dp[i + 1][j - 1]
            dp[i + 1][j] %= MOD

    print(dp[N][B[N - 1]])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 1
    for i in range(n):
        ans *= max(0,b[i]-a[i]+1)
        ans %= 998244353
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    ans = 1
    for i in range(N):
        ans *= max(0, min(B) - max(A) + 1)
        ans %= 998244353
    print(ans)

=======
Suggestion 9

def main():
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    #print(N)
    #print(A)
    #print(B)
    #print(len(A))
    #print(len(B))
    C=[]
    for i in range(N):
        C.append(0)
    #print(C)
    #print(len(C))
    #print(C[0])
    #print(C[1])
    #print(C[2])
    #print(C[3])
    #print(C[4])
    #print(C[5])
    #print(C[6])
    #print(C[7])
    #print(C[8])
    #print(C[9])
    #print(C[10])
    #print(C[11])
    #print(C[12])
    #print(C[13])
    #print(C[14])
    #print(C[15])
    #print(C[16])
    #print(C[17])
    #print(C[18])
    #print(C[19])
    #print(C[20])
    #print(C[21])
    #print(C[22])
    #print(C[23])
    #print(C[24])
    #print(C[25])
    #print(C[26])
    #print(C[27])
    #print(C[28])
    #print(C[29])
    #print(C[30])
    #print(C[31])
    #print(C[32])
    #print(C[33])
    #print(C[34])
    #print(C[35])
    #print(C[36])
    #print(C[37])
    #print(C[38])
    #print(C[39])
    #print(C[40])
    #print(C[41])
    #print(C[42])
    #print(C[43])
    #print(C[44])
    #print(C[45])
    #print(C[46])
    #print(C[47])
    #print(C[48])
    #print(C[49])
    #print(C[50])
    #print(C[51])
    #print(C[52])
    #print(C[53])
    #print(C[54])
    #print(C[55])
    #print(C[56])
    #print(C[57])
    #print(C[58])
    #print(C[59])
