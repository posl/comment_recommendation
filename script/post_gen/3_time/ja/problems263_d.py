Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if A[i] > R:
            ans += R
        elif A[i] < L:
            ans += L
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 2

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        if A[i] < L:
            sum += L
        elif A[i] > R:
            sum += R
        else:
            sum += A[i]
    print(sum)

=======
Suggestion 3

def main():
    N,L,R=map(int,input().split())
    A=list(map(int,input().split()))
    dp=[[0,0] for i in range(N+1)]
    for i in range(N):
        dp[i+1][0]=max(dp[i][0]+A[i]*L,dp[i][1]+A[i]*R)
        dp[i+1][1]=max(dp[i][0]+A[i]*R,dp[i][1]+A[i]*L)
    print(max(dp[N][0],dp[N][1]))

=======
Suggestion 4

def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    A = sorted(A)
    #print(A)
    ans = 0
    for i in range(N):
        if A[i] < 0:
            ans += L
        else:
            ans += R
    print(ans)

=======
Suggestion 5

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [-x for x in A]
    ans = 0
    for i in range(N):
        if A[i] < L:
            ans += L
        elif A[i] > R:
            ans += R
        else:
            ans += A[i]
    print(ans)

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    #print(N, L, R)
    #print(A)
    #print(sum(A))
    #print(A[N//2])
    #print(A[N//2-1])
    if L >= 0:
        print(sum(A) + (N//2)*L)
    elif R <= 0:
        print(sum(A) + (N//2)*R)
    else:
        if A[N//2] >= 0:
            print(sum(A[:N//2]) + sum(A[N//2:]) + (N//2)*L)
        elif A[N//2-1] <= 0:
            print(sum(A[:N//2]) + sum(A[N//2:]) + (N//2)*R)
        else:
            print(sum(A[:N//2]) + sum(A[N//2:]) + (N//2)*L + (N//2)*R)

=======
Suggestion 7

def main():
    #入力
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    #x=0,y=0
    ans = sum(A)
    #x=0,y=1
    ans = min(ans,sum(A[:-1])+min(A[-1]*R,R))
    #x=1,y=0
    ans = min(ans,sum(A[1:])+min(A[0]*L,L))
    #x=1,y=1
    ans = min(ans,sum(A[1:-1])+min(A[0]*L,L)+min(A[-1]*R,R))
    #x=0,y=2
    ans = min(ans,sum(A[:-2])+min(A[-2]*R,R)+min(A[-1]*R,R))
    #x=2,y=0
    ans = min(ans,sum(A[2:])+min(A[0]*L,L)+min(A[1]*L,L))
    #x=1,y=2
    ans = min(ans,sum(A[1:-2])+min(A[0]*L,L)+min(A[-2]*R,R)+min(A[-1]*R,R))
    #x=2,y=1
    ans = min(ans,sum(A[2:-1])+min(A[0]*L,L)+min(A[1]*L,L)+min(A[-1]*R,R))
    #x=2,y=2
    ans = min(ans,sum(A[2:-2])+min(A[0]*L,L)+min(A[1]*L,L)+min(A[-2]*R,R)+min(A[-1]*R,R))
    #出力
    print(ans)

=======
Suggestion 8

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #A = [0] + A + [0]
    #N += 2
    #dp = [[0] * (N+1) for _ in range(N+1)]
    #dp[0][0] = sum(A)
    #for i in range(N):
    #    for j in range(i+1):
    #        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + L)
    #        dp[i+1][j] = max(dp[i+1][j], dp[i][j] + R)
    #print(max(dp[N]))
    A.sort()
    ans = 0
    for i in range(N):
        if i < N/2:
            ans += L
        else:
            ans += R
    print(ans)

=======
Suggestion 9

def main():
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    # 0 から n までの部分列について、それぞれの部分列の要素の総和の最小値を求める
    # dp[i][j] := 部分列 a[i:j] の要素の総和の最小値
    # dp[i][j] = min(dp[i][k] + dp[k][j]) (i <= k < j)
    dp = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][i] = 0
    for width in range(1, n + 1):
        for i in range(n + 1 - width):
            j = i + width
            for k in range(i + 1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            dp[i][j] += sum(a[i:j])
    # dp[i][j] を使って、部分列 a[0:n] の要素の総和の最小値を求める
    # dp[i][j] を使って、部分列 a[i:n] の要素の総和の最小値を求める
    # dp[i][j] を使って、部分列 a[0:j] の要素の総和の最小値を求める
    # dp[i][j] を使って、部分列 a[i:j] の要素の総和の最小値を求める
    ans = min(dp[0][n], dp[0][n] + l, dp[0][n] + r, dp[0][n] + l + r)
    for i in range(n):
        ans = min(ans, dp[0][i] + dp[i][n] + r)
    for i in range(n):
        ans = min(ans, dp[0][i] + dp[i][n] + l)
    for i in range

=======
Suggestion 10

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    # 0 は L に置き換える
    # N は R に置き換える
    # 0 と N 以外は L と R のどちらか小さい方に置き換える
    # 0 と N 以外をすべて L に置き換える
    # 0 と N 以外をすべて R に置き換える

    # 0 と N 以外をすべて L に置き換える
    ans1 = 0
    for i in range(N):
        ans1 += min(A[i], L)

    # 0 と N 以外をすべて R に置き換える
    ans2 = 0
    for i in range(N):
        ans2 += min(A[i], R)

    # 0 は L に置き換える
    # N は R に置き換える
    # 0 と N 以外は L と R のどちらか小さい方に置き換える
    ans3 = 0
    for i in range(N):
        if i < N // 2:
            ans3 += min(A[i], L)
        else:
            ans3 += min(A[i], R)

    print(min(ans1, ans2, ans3))
