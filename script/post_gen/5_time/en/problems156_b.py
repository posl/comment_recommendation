Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        n //= k
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    count = 0
    while N > 0:
        N = N // K
        count += 1
    print(count)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    count = 0
    while n > 0:
        n = n // k
        count += 1
    print(count)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    count = 0
    while N > 0:
        N //= K
        count += 1
    print(count)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        ans += 1
        n = n // k
    print(ans)

=======
Suggestion 6

def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    count = 0
    while N > 0:
        N = N // K
        count += 1
    print(count)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    ans = 0
    while N != 0:
        ans += 1
        N //= K
    print(ans)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    digit = 0
    while n >= k:
        n = n // k
        digit += 1
    print(digit + 1)
