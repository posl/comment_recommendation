Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000
    for T in range(1, N):
        S1 = sum(W[:T])
        S2 = sum(W[T:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 2

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 100000000
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    ws = [int(x) for x in input().split()]
    min = 100000
    for i in range(1, n):
        s1 = sum(ws[:i])
        s2 = sum(ws[i:])
        if abs(s1 - s2) < min:
            min = abs(s1 - s2)
    print(min)

main()

=======
Suggestion 4

def get_min_abs_diff(n, weights):
    min_abs_diff = 100000
    for i in range(1, n):
        left = weights[:i]
        right = weights[i:]
        left_sum = sum(left)
        right_sum = sum(right)
        abs_diff = abs(left_sum - right_sum)
        if abs_diff < min_abs_diff:
            min_abs_diff = abs_diff
    return min_abs_diff

=======
Suggestion 5

def get_min_weight_diff(n, w):
    min_diff = 1000000000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        if abs(s1 - s2) < min_diff:
            min_diff = abs(s1 - s2)

    return min_diff

=======
Suggestion 6

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 10000
    for i in range(1, n):
        ans = min(ans, abs(sum(w[:i]) - sum(w[i:])))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000000000000000000
    for i in range(1, N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 8

def solve():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 100 * 100
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        ans = min(ans, abs(s1 - s2))
    print(ans)
solve()

=======
Suggestion 9

def main():
    n = int(input())
    w = [int(x) for x in input().split()]
    ans = 10000
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        if abs(s1-s2) < ans:
            ans = abs(s1-s2)
    print(ans)
