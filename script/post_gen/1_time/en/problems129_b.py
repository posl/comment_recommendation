Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = float("inf")
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
    print(ans)

main()

=======
Suggestion 2

def main():
    n = int(input())
    w = [int(x) for x in input().split()]
    s1 = w[0]
    s2 = sum(w[1:])
    ans = abs(s1 - s2)
    for i in range(1, n - 1):
        s1 += w[i]
        s2 -= w[i]
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S1 = 0
    S2 = sum(W)
    min_diff = S2 - S1
    for i in range(1, N):
        S1 += W[i-1]
        S2 -= W[i-1]
        min_diff = min(min_diff, abs(S1 - S2))
    print(min_diff)

=======
Suggestion 4

def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = sum(w)
    s2 = 0
    ans = 1000
    for i in range(n-1):
        s1 -= w[i]
        s2 += w[i]
        ans = min(ans, abs(s1-s2))
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    w = list(map(int, input().split()))

    min_diff = 100 * 100
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff

    print(min_diff)

=======
Suggestion 6

def main():
    n = int(input())
    w = [int(i) for i in input().split()]
    min_diff = 10000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 7

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10000000000000
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    W = [int(w) for w in input().split()]
    S1 = 0
    S2 = sum(W)
    min_diff = 10**6
    for i in range(N-1):
        S1 += W[i]
        S2 -= W[i]
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 9

def get_input():
    N = int(input())
    W = [int(x) for x in input().split()]
    return N, W

=======
Suggestion 10

def main():
    # Read input
    N = int(input())
    W = [int(x) for x in input().split()]

    # Find the minimum possible absolute difference of S_1 and S_2
    ans = sum(W)
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))

    # Output the answer
    print(ans)
