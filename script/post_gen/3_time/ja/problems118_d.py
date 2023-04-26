Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N + 1)
    dp[0] = 0
    for i in range(N + 1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + a <= N:
                dp[i + a] = max(dp[i + a], dp[i] * 10 + a)
    print(dp[N])

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        if dp[i] < 0:
            continue
        for a in A:
            if i + a <= N:
                dp[i+a] = max(dp[i+a], dp[i]*10+a)
    print(dp[N])

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    dp = [-1] * (N+1)
    dp[0] = 0
    for i in range(N+1):
        if dp[i] == -1:
            continue
        for a in A:
            if i + a <= N:
                dp[i+a] = max(dp[i+a], dp[i]*10 + a)
    print(dp[N])

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0
    for i in range(n + 1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i], dp[i - a[j]] + 1)
    ans = ""
    while n > 0:
        for j in range(m):
            if n - a[j] >= 0 and dp[n - a[j]] == dp[n] - 1:
                ans += str(a[j])
                n -= a[j]
                break
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = ''
    while N > 0:
        for i in range(M):
            if N - (A[i] - 1) * 2 >= 0:
                ans += str(A[i])
                N -= (A[i] - 1) * 2
                break
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # Aの値が大きい順にソート
    A.sort(reverse=True)
    # dp[i] := i本のマッチ棒を使って作れる整数の最大値
    dp = [0] * (N + 1)
    # dp[0] = 0
    dp[0] = 0
    # dp[1] = 0
    dp[1] = 0
    # dp[2] = 1
    dp[2] = 1
    # dp[3] = 7
    dp[3] = 7
    # dp[4] = 4
    dp[4] = 4
    # dp[5] = 2
    dp[5] = 2
    # dp[6] = 6
    dp[6] = 6
    # dp[7] = 8
    dp[7] = 8
    # dp[8] = 10
    dp[8] = 10
    # dp[9] = 18
    dp[9] = 18
    # dp[10] = 22
    dp[10] = 22
    # dp[11] = 20
    dp[11] = 20
    # dp[12] = 28
    dp[12] = 28
    # dp[13] = 68
    dp[13] = 68
    # dp[14] = 88
    dp[14] = 88
    # dp[15] = 108
    dp[15] = 108
    # dp[16] = 188
    dp[16] = 188
    # dp[17] = 200
    dp[17] = 200
    # dp[18] = 208
    dp[18] = 208
    # dp[19] = 288
    dp[19] = 288
    # dp[20] = 688
    dp[20] = 688
    # dp[21] = 888
    dp

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    # print(a)
    dp = [-1] * (n + 1)
    dp[0] = 0
    for i in range(n):
        if dp[i] == -1:
            continue
        for j in range(m):
            if i + a[j] <= n:
                dp[i + a[j]] = max(dp[i + a[j]], dp[i] * 10 + a[j])
    print(dp[n])

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    #print(n,m,a)
    a.sort(reverse=True)
    #print(a)
    dp = [-1]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        for j in range(m):
            if i - a[j] >= 0:
                dp[i] = max(dp[i],dp[i-a[j]] + 1)
    #print(dp)
    ans = ""
    for i in range(dp[n]):
        for j in range(m):
            if n - a[j] >= 0 and dp[n] == dp[n-a[j]] + 1:
                ans += str(a[j])
                n -= a[j]
                break
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    #dp[i]:整数iを作るために使うマッチ棒の本数
    dp = [-1] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        for j in range(M):
            if i - A[j] >= 0 and dp[i - A[j]] != -1:
                dp[i] = max(dp[i], dp[i - A[j]] + 1)

    #dp[N]が-1の場合は作れない
    if dp[N] == -1:
        print(-1)
        return

    #dp[N]が0の場合は0しか作れない
    if dp[N] == 0:
        print(0)
        return

    #dp[N]が1以上の場合はdp[i]が最大のiを見つける
    #dp[1]が最大の場合は1を作れる
    #dp[2]が最大の場合は11を作れる
    #dp[3]が最大の場合は111を作れる
    #dp[4]が最大の場合は1111を作れる
    #dp[5]が最大の場合は11111を作れる
    #dp[6]が最大の場合は111111を作れる
    #dp[7]が最大の場合は1111111を作れる
    #dp[8]が最大の場合は11111111を作れる
    #dp[9]が最大の場合は111111111を作れる
    #dp[10]が最大の場合は1111111111を作れる
    #dp[11]が最大の場合は11111111111を作れる
    #dp[12]が最大の場合は111111111111を作れる
    #dp[13]が最大の場合は1111111111111を作れ
