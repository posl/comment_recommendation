Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000
    for i in range(1, N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 2

def main():
    N = int(input())
    W = list(map(int, input().split()))
    result = 10000
    for i in range(1, N):
        result = min(result, abs(sum(W[:i]) - sum(W[i:])))
    print(result)

=======
Suggestion 3

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000
    for i in range(1,N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 4

def main():
    n = int(input())
    w = list(map(int, input().split()))
    w_sum = sum(w)
    for i in range(n):
        s1 = sum(w[:i+1])
        s2 = w_sum - s1
        print(abs(s1 - s2))
    return

=======
Suggestion 5

def solve():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    s1 = 0
    ans = S
    for w in W:
        s1 += w
        s2 = S - s1
        ans = min(ans, abs(s1 - s2))
    return ans

print(solve())

=======
Suggestion 6

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 10000000000
    for i in range(n):
        ans = min(ans, abs(sum(w[:i+1]) - sum(w[i+1:])))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000000
    for i in range(N):
        S1 = sum(W[:i+1])
        S2 = sum(W[i+1:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 8

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000
    for i in range(0, N):
        S1 = sum(W[0:i+1])
        S2 = sum(W[i+1:N])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 9

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000000000000
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 10

def solve():
    N = int(input())
    W = list(map(int, input().split()))

    min = 100 * 100
    for t in range(1, N):
        S1 = sum(W[:t])
        S2 = sum(W[t:])
        diff = abs(S2 - S1)
        if diff < min:
            min = diff

    print(min)
