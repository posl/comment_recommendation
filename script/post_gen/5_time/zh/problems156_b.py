Synthesizing 10/10 solutions

=======
Suggestion 1

def convert_to_base(n, base):
    result = ''
    while n > 0:
        result = str(n % base) + result
        n //= base
    return result


n, k = map(int, input().split())
print(len(convert_to_base(n, k)))

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    cnt = 0
    while n > 0:
        n //= k
        cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    cnt = 0
    while n > 0:
        cnt += 1
        n = n // k
    print(cnt)

=======
Suggestion 4

def get_digit(n, k):
    if n == 0:
        return 0
    return get_digit(n//k, k) + 1

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    count = 0
    while N > 0:
        N = N // K
        count += 1
    print(count)

=======
Suggestion 6

def solution(n, k):
    ans = 0
    while n > 0:
        n //= k
        ans += 1
    return ans

=======
Suggestion 7

def get_digits(num, base):
    digits = 0
    while num > 0:
        digits += 1
        num //= base
    return digits

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    count = 0
    while n >= k:
        count += 1
        n //= k
    print(count + 1)

main()

=======
Suggestion 9

def main():
    n,k = map(int,input().split())
    count = 0
    while n > 0:
        n = n//k
        count += 1
    print(count)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    ans = 0
    while n != 0:
        n //= k
        ans += 1
    print(ans)
