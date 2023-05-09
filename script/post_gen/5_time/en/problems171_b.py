Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:K]))

=======
Suggestion 3

def solve(N, K, p):
    p.sort()
    return sum(p[:K])

N, K = map(int, input().split())
p = list(map(int, input().split()))
print(solve(N, K, p))

=======
Suggestion 4

def solve():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = 0
    for i in range(k):
        ans += p[i]
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    print(sum(p[:k]))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort()
    print(sum(P[:K]))

=======
Suggestion 7

def problems171_b():
    n, k = map(int, input().split())
    p = sorted(list(map(int, input().split())))
    print(sum(p[:k]))

=======
Suggestion 8

def solve(N, K, p):
    p.sort()
    return sum(p[:K])

=======
Suggestion 9

def solve(n,k,prices):
    prices.sort()
    return sum(prices[:k])
