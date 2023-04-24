Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    W = list(map(int, input().split()))

=======
Suggestion 2

def main():
    N = int(input())
    W = list(map(int, input().split()))
    # N = 8
    # W = [27, 23, 76, 2, 3, 5, 62, 52]
    # N = 4
    # W = [1, 3, 1, 1]
    # N = 3
    # W = [1, 2, 3]
    # N = 2
    # W = [1, 1]
    # print(N)
    # print(W)

    S1 = 0
    S2 = 0
    diff = 0
    min_diff = 0
    for i in range(N):
        S1 = sum(W[0:i + 1])
        S2 = sum(W[i + 1:N])
        # print(S1)
        # print(S2)
        diff = abs(S1 - S2)
        if i == 0:
            min_diff = diff
        elif diff < min_diff:
            min_diff = diff
        # print(diff)
        # print(min_diff)
    print(min_diff)

=======
Suggestion 3

def main():
    N = int(input())
    W = list(map(int, input().split()))

    S1 = 0
    S2 = sum(W)
    ans = S2

    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        ans = min(ans, abs(S1-S2))

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    W = list(map(int, input().split()))
    W = [0] + W
    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + W[i]
    ans = 10**9
    for i in range(1, N):
        ans = min(ans, abs(S[N] - 2 * S[i]))
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    W = [int(i) for i in input().split()]
    S = sum(W)
    ans = S
    for i in range(1, N):
        ans = min(ans, abs(2 * sum(W[:i]) - S))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    W = list(map(int, input().split()))
    if N == 2:
        print(abs(W[0] - W[1]))
        return
    sumW = sum(W)
    minDif = 1000000000000000000
    for i in range(1, N):
        sumW1 = sum(W[:i])
        sumW2 = sumW - sumW1
        minDif = min(minDif, abs(sumW1 - sumW2))
    print(minDif)

=======
Suggestion 7

def main():
    N = int(input())
    W = list(map(int, input().split()))
    # 累積和を求める
    W_sum = [0] * (N+1)
    for i in range(N):
        W_sum[i+1] = W_sum[i] + W[i]
    # 差の絶対値の最小値を求める
    ans = float("inf")
    for T in range(1, N):
        ans = min(ans, abs(W_sum[T] - (W_sum[N] - W_sum[T])))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    W = list(map(int, input().split()))
    W = [0] + W
    S = sum(W)
    S1 = 0
    S2 = S
    ans = 10**10
    for i in range(1, N+1):
        S1 += W[i]
        S2 -= W[i]
        ans = min(ans, abs(S1-S2))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    W = list(map(int, input().split()))
    # 累積和
    W_sum = []
    W_sum.append(W[0])
    for i in range(1, N):
        W_sum.append(W_sum[i-1] + W[i])
    ans = 10000
    for i in range(1, N):
        ans = min(ans, abs(W_sum[i-1] - (W_sum[N-1] - W_sum[i-1])))
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    W = list(map(int, input().split()))
    #print(N, W)
    W_sum = sum(W)
    #print(W_sum)
    S1 = 0
    S2 = 0
    min
