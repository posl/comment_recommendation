Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = 0
    s2 = sum(w)
    ans = s2
    for i in range(n-1):
        s1 += w[i]
        s2 -= w[i]
        ans = min(abs(s1-s2), ans)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    W = list(map(int, input().split()))

    ans = float("inf")
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))

    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    w = list(map(int, input().split()))

    ans = float('inf')
    for i in range(1, n):
        ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    diff = S2 - S1
    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        diff = min(diff, abs(S2-S1))
    print(diff)

=======
Suggestion 5

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        ans = min(ans, abs(S1-S2))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    min_diff = S2 - S1
    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        diff = abs(S1 - S2)
        min_diff = min(min_diff, diff)
    print(min_diff)

=======
Suggestion 7

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000
    for i in range(1, N):
        sum1 = sum(W[:i])
        sum2 = sum(W[i:])
        diff = abs(sum1 - sum2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 8

def main():
    N = int(input())
    W = list(map(int, input().split()))
    T = 1
    S1 = 0
    S2 = 0
    while T < N:
        for i in range(T):
            S1 += W[i]
        for j in range(T, N):
            S2 += W[j]
        T += 1
        print(abs(S1 - S2))

=======
Suggestion 9

def main():
    N = int(input())
    W = [int(i) for i in input().split()]
    W_sum = sum(W)
    W_sum_half = W_sum // 2
    dp = [[False] * (W_sum_half + 1) for i in range(N + 1)]
    dp[0][0] = True
    for i in range(N):
        for j in range(W_sum_half + 1):
            if j < W[i]:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = dp[i][j] or dp[i][j - W[i]]
    for j in range(W_sum_half, -1, -1):
        if dp[N][j]:
            print(W_sum - 2 * j)
            break

=======
Suggestion 10

def main():
    # 入力
    N = int(input())
    W = list(map(int, input().split()))

    # 処理
    min = 1000
    for i in range(1, N):
        W1 = sum(W[:i])
        W2 = sum(W[i:])
        if abs(W1 - W2) < min:
            min = abs(W1 - W2)

    # 出力
    print(min)
