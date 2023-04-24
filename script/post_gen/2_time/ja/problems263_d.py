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
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] >= 0:
            if i > 0:
                ans += A[i] * min(i, L)
            if N - i > 0:
                ans += A[i] * min(N - i, R)
        else:
            if i > 0:
                ans += A[i] * min(i, R)
            if N - i > 0:
                ans += A[i] * min(N - i, L)
    print(ans)

main()

=======
Suggestion 3

def main():
    N,L,R = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        if A[i] < 0:
            ans += L
        else:
            ans += R
    print(ans)

=======
Suggestion 4

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [-A[i] if i % 2 == 0 else A[i] for i in range(N)]
    print(sum(A) - sum(A[:N // 2]) * (L - R) + R * N // 2 - L * (N - N // 2))

=======
Suggestion 5

def main():
    #入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    #処理
    #累積和
    sumA = [0]
    for i in range(N):
        sumA.append(sumA[i]+A[i])
    #print(sumA)

    #最小値
    minA = sumA[N]
    #print(minA)

    #x=0,y=0
    if minA > L:
        minA = L
    if minA > R:
        minA = R
    #print(minA)

    #x=1,y=1
    for i in range(1, N+1):
        if minA > L + sumA[i]:
            minA = L + sumA[i]
        if minA > R + sumA[N]-sumA[N-i]:
            minA = R + sumA[N]-sumA[N-i]
    #print(minA)

    #x=0,y=1
    for i in range(1, N+1):
        if minA > R + sumA[N]-sumA[N-i]:
            minA = R + sumA[N]-sumA[N-i]
    #print(minA)

    #x=1,y=0
    for i in range(1, N+1):
        if minA > L + sumA[i]:
            minA = L + sumA[i]
    #print(minA)

    #x=0,y=2
    for i in range(1, N):
        if minA > 2*R + sumA[N]-sumA[N-i]:
            minA = 2*R + sumA[N]-sumA[N-i]
    #print(minA)

    #x=2,y=0
    for i in range(1, N):
        if minA > 2*L + sumA[i]:
            minA = 2*L + sumA[i]
    #print(minA)

    #x=1,y=2
    for i in range(1, N):
        for j in range(1, N-i+1):
            if minA > L + 2*R + sumA[N]-sumA[N-i]-sumA[N-i-j]:
                minA = L + 2

=======
Suggestion 6

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    sumA = sum(A)
    A = [min(L, R)] * N
    print(sumA - sum(A))

=======
Suggestion 7

def main():
    #入力
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    #初期化
    #dp[i][0] : i番目までの要素を操作した後に、左からi番目の要素をLに置き換えた時の最大値
    #dp[i][1] : i番目までの要素を操作した後に、左からi番目の要素をRに置き換えた時の最大値
    #dp[i][2] : i番目までの要素を操作した後に、左からi番目の要素をそのままにする時の最大値
    dp = [[0] * 3 for _ in range(N + 1)]
    dp[0][0] = L
    dp[0][1] = R
    dp[0][2] = 0

    #漸化式
    for i in range(N):
        dp[i + 1][0] = max(dp[i][0] + A[i], dp[i][1] + A[i], dp[i][2] + L)
        dp[i + 1][1] = max(dp[i][0] + R, dp[i][1] + A[i], dp[i][2] + A[i])
        dp[i + 1][2] = max(dp[i][0], dp[i][1], dp[i][2] + A[i])

    #出力
    print(dp[N][0])

=======
Suggestion 8

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    # 0 から N までの総和を求める
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        s[i] = s[i - 1] + A[i - 1]

    # 0 から i までの総和を求める
    # 0 から i までの総和の最小値を求める
    # 0 から i までの総和の最小値の最大値を求める
    # 0 から i までの総和の最小値の最大値と s[i] の差が最大となる i を求める
    # その差が答え
    ans = -float('inf')
    for i in range(N + 1):
        ans = max(ans, s[i] - min(s[:i + 1]))
    print(ans + L + R)

=======
Suggestion 9

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    # AをLで置き換える
    for i in range(N):
        if L < A[i]:
            A[i] = L

    # AをRで置き換える
    for i in range(N-1, -1, -1):
        if A[i] > R:
            A[i] = R

    print(sum(A))

=======
Suggestion 10

def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))

    # 0 を含む区間の最大値
    max_sum = 0
    # 0 以外の区間の最大値
    max_sum2 = 0
    # 0 を含む区間の最小値
    min_sum = 0
    # 0 以外の区間の最小値
    min_sum2 = 0

    # 区間の最大値、最小値を求める
    for i in range(N):
        max_sum += max(L, A[i])
        min_sum += min(R, A[i])
        if A[i] != 0:
            max_sum2 += max(L, A[i])
            min_sum2 += min(R, A[i])

    # 0 を含む区間の最大値と最小値の差
    diff = max_sum - min_sum

    # 0 以外の区間の最大値と最小値の差
    diff2 = max_sum2 - min_sum2

    # 0 を含む区間の最大値と最小値の差が 0 でない場合
    if diff != 0:
        # 0 以外の区間の最大値と最小値の差を 0 にする
        # 最大値と最小値の差の絶対値を 2 で割った値を、
        # 0 以外の区間の最大値と最小値の差に足す
        # 0 以外の区間の最大値と最小値の差が 0 になる
        ans = max_sum2 - min_sum2 + abs(diff) // 2
    # 0 を含む区間の最大値と最小値の差が 0 の場合
    else:
        # 0 以外の区間の最大値と最
