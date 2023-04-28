Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = float('inf')
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10000
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    S1 = 0
    S2 = S
    for i in range(N):
        S1 += W[i]
        S2 -= W[i]
        if abs(S1 - S2) > abs(S1 - S//2):
            S1 -= W[i]
            S2 += W[i]
    print(abs(S1 - S2))

=======
Suggestion 4

def main():
    n = int(input())
    w = list(map(int, input().split()))
    min_diff = 1000
    for i in range(n):
        diff = abs(sum(w[:i+1]) - sum(w[i+1:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 5

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 100000
    for i in range(n):
        ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    S1 = 0
    S2 = S
    for t in range(N):
        S1 += W[t]
        S2 -= W[t]
        if abs(S1-S2) > abs(S1-W[t]-S2+W[t]):
            S1 -= W[t]
            S2 += W[t]
    print(abs(S1-S2))

=======
Suggestion 7

def main():
    n = int(input())
    w = list(map(int, input().split()))
    w_sum = sum(w)
    min_diff = w_sum
    for i in range(n):
        s1 = sum(w[:i+1])
        s2 = w_sum - s1
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 8

def main():
    N = int(input())
    W = list(map(int, input().split()))
    sumW = sum(W)
    minDiff = sumW
    for i in range(1, N):
        sum1 = sum(W[:i])
        sum2 = sumW - sum1
        diff = abs(sum1 - sum2)
        if diff < minDiff:
            minDiff = diff
    print(minDiff)

=======
Suggestion 9

def main():
    N = int(input())
    W = list(map(int, input().split()))
    W_sum = sum(W)
    W_sum1 = 0
    W_sum2 = 0
    for i in range(N):
        W_sum1 += W[i]
        W_sum2 = W_sum - W_sum1
        if i == 0:
            min_diff = abs(W_sum1 - W_sum2)
        elif abs(W_sum1 - W_sum2) < min_diff:
            min_diff = abs(W_sum1 - W_sum2)
    print(min_diff)

=======
Suggestion 10

def solve(N,W):
    S1 = sum(W)
    S2 = 0
    for i in range(N):
        S2 += W[i]
        S1 -= W[i]
        if abs(S2-S1) < diff:
            diff = abs(S2-S1)
    return diff

N = int(input())
W = list(map(int,input().split()))
print(solve(N,W))
