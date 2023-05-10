Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 10**9
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10000
    for i in range(1, N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    w = list(map(int, input().split()))
    s = sum(w)
    ans = s
    s1 = 0
    s2 = 0
    for t in range(1, n):
        s1 += w[t-1]
        s2 = s - s1
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    W = list(map(int, input().split()))
    #print(N)
    #print(W)
    ans = 1000000000
    for i in range(1, N):
        s1 = sum(W[:i])
        s2 = sum(W[i:])
        #print(s1, s2)
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 5

def solve():
    n = int(input())
    ws = list(map(int, input().split()))
    result = 100000000000000
    for i in range(1, n):
        s1 = sum(ws[:i])
        s2 = sum(ws[i:])
        result = min(result, abs(s1 - s2))
    print(result)

=======
Suggestion 6

def main():
    #n = int(input())
    #a = [int(x) for x in input().split()]
    n = 8
    a = [27,23,76,2,3,5,62,52]
    print(min([abs(sum(a[:t]) - sum(a[t:])) for t in range(1,n)]))

=======
Suggestion 7

def main():
    n = int(input())
    w = list(map(int, input().split()))
    result = 100000
    for i in range(1, n):
        s1 = sum(w[:i])
        s2 = sum(w[i:])
        result = min(result, abs(s1 - s2))
    print(result)

=======
Suggestion 8

def main():
    N = int(input())
    W = list(map(int, input().split()))
    ans = 10000
    for i in range(1, N):
        ans = min(ans, abs(sum(W[:i]) - sum(W[i:])))
    print(ans)

=======
Suggestion 9

def main():
    n = int(input())
    w = list(map(int, input().split()))
    s1 = 0
    s2 = sum(w)
    ans = s2
    for i in range(n):
        s1 += w[i]
        s2 -= w[i]
        ans = min(ans, abs(s1 - s2))
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    w = list(map(int, input().split()))
    ans = 1000000000
    for t in range(1, n):
        s1 = sum(w[:t])
        s2 = sum(w[t:])
        ans = min(ans, abs(s1 - s2))
    print(ans)
