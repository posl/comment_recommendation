Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    i = 1
    while N >= K:
        N //= K
        i += 1
    print(i)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    count = 0
    while n > 0:
        n = n // k
        count += 1
    print(count)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    i = 0
    while N >= K:
        N = N // K
        i += 1
    print(i + 1)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())

    i = 0
    while n > 0:
        n = n // k
        i += 1

    print(i)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    # print(n,k)
    # print(type(n),type(k))
    count = 0
    while n > 0:
        n = n//k
        count += 1
    print(count)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    i = 0
    while n >= k:
        n = n // k
        i += 1
    print(i+1)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    count = 0
    while n >= k:
        n = n // k
        count += 1
    print(count+1)

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    count = 0
    while True:
        n = n // k
        count += 1
        if n == 0:
            break
    print(count)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        ans += 1
        n //= k
    print(ans)
