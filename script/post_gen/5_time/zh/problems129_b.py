Synthesizing 10/10 solutions

=======
Suggestion 1

def min_diff(n, w):
    min_diff = 10

=======
Suggestion 2

def get_input():
    N = int(input())
    W = [int(i) for i in input().split()]
    return N, W

=======
Suggestion 3

def main():
    N = int(input())
    w = list(map(int, input().split()))
    w.sort()
    t = sum(w)
    s = 0
    for i in range(N-1):
        s += w[i]
        if s*2 >= t:
            print(min(s*2-t, t-s*2+w[i+1]))
            break

=======
Suggestion 4

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 1000
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        ans = min(ans, abs(s1-s2))
    print(ans)

=======
Suggestion 5

def problems129_b():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000000000
    for i in range(1, N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 6

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min = 10000
    for i in range(1, N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        if abs(s1-s2) < min:
            min = abs(s1-s2)
    print(min)

=======
Suggestion 7

def main():
    # input
    N = int(input())
    W = list(map(int,input().split()))

    # processing
    W_sum = sum(W)
    S_1 = 0
    S_2 = W_sum
    min_diff = W_sum
    for i in range(N):
        S_1 += W[i]
        S_2 -= W[i]
        diff = abs(S_1 - S_2)
        if diff < min_diff:
            min_diff = diff

    # output
    print(min_diff)

=======
Suggestion 8

def solve():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 100000000
    for t in range(1, N):
        s1, s2 = 0, 0
        for i in range(t):
            s1 += W[i]
        for i in range(t, N):
            s2 += W[i]
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 9

def search_min_diff(n, w):
    min_diff = 100 * 100
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        diff = abs(s1 - s2)
        if min_diff > diff:
            min_diff = diff
    return min_diff

=======
Suggestion 10

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    T = 100000
    for i in range(N):
        T = min(T, abs(S - 2 * sum(W[:i+1])))
    print(T)
