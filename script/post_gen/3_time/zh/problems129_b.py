Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    ans = S
    S1 = 0
    for i in range(N):
        S1 += W[i]
        S2 = S - S1
        ans = min(ans, abs(S1 - S2))
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    w = list(map(int, input().split()))
    w.sort()
    w1 = w[:n//2]
    w2 = w[n//2:]
    print(abs(sum(w1) - sum(w2)))

=======
Suggestion 3

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min = 100000000000
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        if abs(S1 - S2) < min:
            min = abs(S1 - S2)
    print(min)

=======
Suggestion 4

def search(n):
    w = list(map(int, input().split()))
    w.sort()
    s1 = 0
    s2 = sum(w)
    ans = s2
    for i in range(n):
        s1 += w[i]
        s2 -= w[i]
        ans = min(ans, abs(s1-s2))
    return ans

=======
Suggestion 5

def main():
    n = int(input())
    w = list(map(int, input().split()))
    result = 100
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        if result > abs(s1 - s2):
            result = abs(s1 - s2)
    print(result)

=======
Suggestion 6

def main():
    N = int(input())
    W = list(map(int, input().split()))
    W.sort()
    T = int(sum(W)/2)
    s1 = 0
    s2 = 0
    for i in range(N):
        if s1 + W[i] <= T:
            s1 += W[i]
        else:
            s2 += W[i]
    print(abs(s2 - s1))

=======
Suggestion 7

def min_diff(n, w):
    min_diff = 100000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    return min_diff

=======
Suggestion 8

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100 * 100
    for i in range(1, N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 9

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 10

def main():
    n = int(input())
    weights = [int(x) for x in input().split()]
    weights.sort()
    sum = 0
    for i in range(n):
        sum += weights[i]
    half = sum / 2
    sum1 = 0
    for i in range(n):
        sum1 += weights[i]
        if sum1 >= half:
            if sum1 - half < half - sum1 + weights[i]:
                print(int(sum1 - half) * 2)
            else:
                print(int(half - sum1 + weights[i]) * 2)
            break
