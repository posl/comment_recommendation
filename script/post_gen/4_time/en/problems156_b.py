Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    cnt = 0
    while N > 0:
        N = N // K
        cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    count = 0
    while N != 0:
        N = N // K
        count += 1
    print(count)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        ans += 1
        N //= K
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    while N > 0:
        N = N//K
        ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    count = 0
    while n >= k:
        n = n // k
        count += 1
    print(count + 1)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    if n == 0:
        print(0)
        return
    result = 0
    while n > 0:
        n //= k
        result += 1
    print(result)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    result = 0
    while N > 0:
        N = N // K
        result += 1
    print(result)

=======
Suggestion 8

def main():
    N,K = map(int, input().split())
    count = 0
    while N >= K:
        N = N // K
        count += 1
    print(count+1)

=======
Suggestion 9

def solve(n,k):
    count = 0
    while n > 0:
        n = n // k
        count += 1
    return count

=======
Suggestion 10

def main():
    N, K = map(int, input().split())
    print(len(str(N))) if K == 10 else print(len(change_base(N, K)))
