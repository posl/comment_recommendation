Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = sum(w)
    for i in range(n):
        s1 = sum(w[:i+1])
        s2 = sum(w[i+1:])
        ans = min(ans, abs(s1-s2))
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 1000000000
    for i in range(1, N):
        S1 = sum(W[:i])
        S2 = sum(W[i:])
        ans = min(ans, abs(S1 - S2))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    w = list(map(int, input().split()))
    result = 1000000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        result = min(result, abs(s1 - s2))
    print(result)

=======
Suggestion 4

def problems129_b():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 1000
    for i in range(1, N):
        diff = abs(sum(W[:i]) - sum(W[i:]))
        if diff < min_diff:
            min_diff = diff
    return min_diff

print(problems129_b())

=======
Suggestion 5

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min_diff = 100000000
    for T in range(1, N):
        S1 = sum(W[:T])
        S2 = sum(W[T:])
        diff = abs(S1 - S2)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)

=======
Suggestion 6

def main():
    N = int(input())
    W = list(map(int, input().split()))
    min = 100000000
    for i in range(1, N):
        S1 = 0
        S2 = 0
        for j in range(0, i):
            S1 += W[j]
        for j in range(i, N):
            S2 += W[j]
        if abs(S1 - S2) < min:
            min = abs(S1 - S2)
    print(min)

=======
Suggestion 7

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 1000000000000
    for i in range(n-1):
        ans = min(ans, abs(sum(w[:i+1]) - sum(w[i+1:])))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    W = list(map(int, input().split()))
    S = sum(W)
    s = 0
    for i in range(N):
        s += W[i]
        if s > S/2:
            print(abs(S-s-s+W[i]))
            break
    else:
        print(abs(S-s-s))

=======
Suggestion 9

def main():
    n = int(input())
    weights = [int(i) for i in input().split()]

    min_diff = sum(weights)
    for t in range(1, n):
        s1 = sum(weights[:t])
        s2 = sum(weights[t:])
        diff = abs(s1 - s2)
        if diff < min_diff:
            min_diff = diff

    print(min_diff)

=======
Suggestion 10

def calc_diff(n, w):
    diff = 10000
    for i in range(1, n):
        s1 = sum(w[0:i])
        s2 = sum(w[i:n])
        if diff > abs(s1 - s2):
            diff = abs(s1 - s2)
    return diff
