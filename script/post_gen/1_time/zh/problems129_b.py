Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    w = list(map(int, input().split()))

=======
Suggestion 2

def main():
    n = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000000000
    for i in range(1, n):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 3

def get_min_diff(N, W):
    min_diff = 10000
    for i in range(1, N):
        sum1 = sum(W[:i])
        sum2 = sum(W[i:])
        if abs(sum1 - sum2) < min_diff:
            min_diff = abs(sum1 - sum2)
    return min_diff

=======
Suggestion 4

def problem129_b():
    N = int(input())
    W = list(map(int,input().split()))
    min = 100000
    for i in range(1,N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        if abs(s1-s2) < min:
            min = abs(s1-s2)
    print(min)

problem129_b()

=======
Suggestion 5

def get_min_diff():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 10000
    for t in range(1, N):
        S1 = sum(W[:t])
        S2 = sum(W[t:])
        min_diff = min(min_diff, abs(S1 - S2))
    return min_diff

=======
Suggestion 6

def problems129_b():
    N = int(input())
    W = [int(i) for i in input().split()]
    min_diff = sum(W)
    for i in range(N):
        S1 = sum(W[0:i+1])
        S2 = sum(W[i+1:N])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 7

def main():
    n = int(input())
    W = list(map(int, input().split()))
    min_diff = 100 * 100
    for i in range(1, n):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        min_diff = min(min_diff, diff)
    print(min_diff)

=======
Suggestion 8

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 100
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000
    for t in range(1, n):
        s1 = sum(W[0:t])
        s2 = sum(W[t:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 10

def get_min_diff(l):
    l.sort()
    T = sum(l)/2
    S1 = 0
    S2 = 0
    for i in range(len(l)):
        if S1 + l[i] <= T:
            S1 += l[i]
        else:
            S2 += l[i]
    return abs(S1 - S2)
