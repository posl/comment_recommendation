Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    count = 0
    while n > 0:
        n = n // k
        count += 1
    print(count)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    cnt = 0
    while n >= k:
        n = n // k
        cnt += 1
    print(cnt+1)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    i = 0
    while n >= k:
        n //= k
        i += 1
    print(i+1)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    print(len(str(N)))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    count = 0
    while n > 0:
        n = n // k
        count += 1
    print(count)

main()

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    digits = 0
    while N > 0:
        N //= K
        digits += 1
    print(digits)

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        ans += 1
        n //= k
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    count = 0
    while N > 0:
        N = N // K
        count += 1
    print(count)
