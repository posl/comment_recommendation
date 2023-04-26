Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    ans = 0
    for i in range(k):
        ans += p[i]
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:k]))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    print(sum(p[:K]))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    print(sum(sorted(p)[:k]))

=======
Suggestion 5

def solve():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))

    p.sort()

    print(sum(p[:K]))
