Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] < 0:
            A[i] = -A[i]
            ans += 2 * A[i] * L
        else:
            ans += 2 * A[i] * R
    ans -= (L + R) * (max(A) - min(A))
    print(ans)
main()

=======
Suggestion 2

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            ans += (a[i] - a[i+1]) * l
            a[i+1] = a[i]
    for i in range(n-1, 0, -1):
        if a[i] > a[i-1]:
            ans += (a[i] - a[i-1]) * r
            a[i-1] = a[i]
    print(ans)

=======
Suggestion 3

def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0
    for i in range(N-1):
        if A[i] > A[i+1]:
            ans += (A[i]-A[i+1])*L
        elif A[i] < A[i+1]:
            ans += (A[i+1]-A[i])*R
    print(ans)

=======
Suggestion 4

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    
    for i in range(N):
        A[i] += A[i-1]
    
    dp = [[float("inf")]*2 for _ in range(N+1)]
    dp[0][0] = 0

    for i in range(N):
        dp[i+1][0] = min(dp[i+1][0], dp[i][0]+A[i]*R+A[i-1]*(L-R))
        dp[i+1][0] = min(dp[i+1][0], dp[i][1]+A[i]*R+A[i-1]*(L-R))
        dp[i+1][1] = min(dp[i+1][1], dp[i][0]+A[i]*L+A[i-1]*(R-L))
        dp[i+1][1] = min(dp[i+1][1], dp[i][1]+A[i]*L+A[i-1]*(R-L))
    
    print(dp[N][0])

=======
Suggestion 5

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(N):
        if A[i] < L:
            A[i] = L
        elif A[i] > R:
            A[i] = R

    print(sum(A))

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] -= R
    #print(A)
    dp = [[0,0] for _ in range(N+1)]
    for i in range(N):
        dp[i+1][0] = min(dp[i][0], dp[i][1])
        dp[i+1][1] = min(dp[i][0], dp[i][1]) + A[i]
    #print(dp)
    print(min(dp[N][0], dp[N][1]) + L * N)
main()

=======
Suggestion 7

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            ans += (a[i] - a[i+1]) * l
            a[i+1] = a[i]
    for i in range(n-1,0,-1):
        if a[i] < a[i-1]:
            ans += (a[i-1] - a[i]) * r
            a[i-1] = a[i]
    print(ans)

=======
Suggestion 8

def main():
    n,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            ans += (a[i]-a[i+1])*l
    for i in range(n-1,0,-1):
        if a[i] > a[i-1]:
            ans += (a[i]-a[i-1])*r
    print(ans)
    return

=======
Suggestion 9

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i]
    if L < 0 and R > 0:
        for i in range(N):
            if A[i] < 0:
                if abs(A[i]) - abs(L) < 0:
                    ans += abs(A[i]) - abs(L)
                    A[i] = L
                else:
                    ans += abs(A[i]) - abs(R)
                    A[i] = R
    elif L < 0 and R <= 0:
        for i in range(N):
            if A[i] < 0:
                ans += abs(A[i]) - abs(L)
                A[i] = L
    elif L >= 0 and R > 0:
        for i in range(N):
            if A[i] > 0:
                ans += abs(A[i]) - abs(R)
                A[i] = R
    print(ans)

main()

=======
Suggestion 10

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A = [0] + A
    # dp[i][0]: i番目までの要素を操作したときの最小値
    # dp[i][1]: i番目までの要素を操作したときの最大値
    dp = [[0, 0] for _ in range(N + 1)]

    for i in range(1, N + 1):
        # dp[i][0]を求める
        # dp[i - 1][0] + A[i] + L
        # dp[i - 1][1] + A[i] + L
        # dp[i - 1][0] + A[i] + R
        # dp[i - 1][1] + A[i] + R
        dp[i][0] = min(dp[i - 1][0] + A[i] + L, dp[i - 1][1] + A[i] + L, dp[i - 1][0] + A[i] + R, dp[i - 1][1] + A[i] + R)
        # dp[i][1]を求める
        # dp[i - 1][0] + A[i] + L
        # dp[i - 1][1] + A[i] + L
        # dp[i - 1][0] + A[i] + R
        # dp[i - 1][1] + A[i] + R
        dp[i][1] = max(dp[i - 1][0] + A[i] + L, dp[i - 1][1] + A[i] + L, dp[i - 1][0] + A[i] + R, dp[i - 1][1] + A[i] + R)

    print(dp[N][0])
