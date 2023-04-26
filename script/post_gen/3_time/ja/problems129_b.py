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
    S1 = W[0]
    S2 = sum(W[1:])
    ans = abs(S1 - S2)
    for i in range(1, N - 1):
        S1 += W[i]
        S2 -= W[i]
        ans = min(ans, abs(S1 - S2))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 100
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    W = list(map(int, input().split()))

    ans = 1000000000
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        ans = min(abs(S1 - S2), ans)

    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    min_diff = 1000000
    for T in range(1, N):
        S1 += W[T-1]
        S2 -= W[T-1]
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 6

def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = 0
    s2 = sum(w)
    min_diff = 1000000000
    for i in range(1, n):
        s1 += w[i - 1]
        s2 -= w[i - 1]
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 7

def main():
    N = int(input())
    W = list(map(int, input().split()))
    #print(N)
    #print(W)
    S = sum(W)
    #print(S)
    S1 = 0
    S2 = S
    min = S
    for T in range(1, N):
        S1 += W[T-1]
        S2 -= W[T-1]
        #print(T, S1, S2)
        if abs(S1 - S2) < min:
            min = abs(S1 - S2)
    print(min)

main()

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 1000000000
    for i in range(N - 1):
        S1 = sum(A[:i + 1])
        S2 = sum(A[i + 1:])
        ans = min(ans, abs(S1 - S2))
    print(ans)

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    W = list(map(int, input().split()))
    #初期化
    S = [0]
    for i in range(N):
        S.append(S[i] + W[i])
    #print(S)
    #差の絶対値の最小値を求める
    ans = float("inf")
    for i in range(1,N):
        ans = min(ans, abs(S[i] - (S[N] - S[i])))
    #出力
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    W = list(map(int,input().split()))

    # 全ての重りを左から右に移動させて、左側の重りの重さの和を計算していく
    # その際に最小値を更新していく
    sum = 0
    min = 100000
    for i in range(N):
        sum += W[i]
        if i < N-1:
            if abs(sum - (sum - W[i])) < min:
                min = abs(sum - (sum - W[i]))

    print(min)
