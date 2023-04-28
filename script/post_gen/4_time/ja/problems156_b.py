Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        n = n // k
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        N //= K
        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        n //= k
        ans += 1
    print(ans)
main()

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    count = 0
    while n != 0:
        n = n // k
        count += 1
    print(count)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    ans = 0

    while n > 0:
        n //= k
        ans += 1

    print(ans)

=======
Suggestion 6

def solve():
    N,K = map(int,input().split())
    ans = 0
    while N > 0:
        N = N // K
        ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    l = 0
    while n >= k:
        n = n // k
        l += 1
    print(l+1)
