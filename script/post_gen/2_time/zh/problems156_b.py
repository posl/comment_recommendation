Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    n,k = map(int, input().split())
    count = 0
    while n != 0:
        n = n // k
        count += 1
    print(count)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    result = 0
    while N > 0:
        result += 1
        N = N // K
    print(result)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    i = 0
    while n >= k:
        n = n // k
        i += 1
    print(i+1)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    count = 0
    while n > 0:
        n = n//k
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

def main():
    n, k = map(int, input().split())
    print(len(str(n)))

=======
Suggestion 7

def get_length(n, k):
    if n == 0:
        return 1
    length = 0
    while n > 0:
        n = n // k
        length += 1
    return length

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    count = 0
    while n >= k:
        n = n // k
        count += 1
    print(count + 1)
    return 0

=======
Suggestion 9

def calc_digit(n, k):
    digit = 0
    while n > 0:
        n //= k
        digit += 1
    return digit
