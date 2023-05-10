Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    while N >= K:
        ans += 1
        N = N // K
    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    #print(n,k)
    count = 0
    while n>=k:
        n = n//k
        count += 1
    print(count+1)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        N //= K
        ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    ans = 0
    while n > 0:
        n //= k
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    count = 0
    while True:
        n //= k
        count += 1
        if n == 0:
            break
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
