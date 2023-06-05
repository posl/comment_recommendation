Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    cnt = 0
    while n > 0:
        n //= k
        cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    i = 0
    while n >= k:
        n = n // k
        i += 1
    print(i+1)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    cnt = 0
    while n != 0:
        n = n // k
        cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    N,K = map(int,input().split())
    count = 0
    while N:
        N = N//K
        count += 1
    print(count)

=======
Suggestion 5

def get_digits(num):
    digits = 0
    while num:
        num //= 10
        digits += 1
    return digits

=======
Suggestion 6

def solve(n, k):
    ans = 0
    while n > 0:
        n //= k
        ans += 1
    return ans

=======
Suggestion 7

def convert(n, k):
    if n < k:
        return str(n)
    else:
        return convert(n//k, k) + str(n%k)

N, K = map(int, input().split())
print(len(convert(N, K)))

=======
Suggestion 8

def getNumOfDigits(number, base):
    numOfDigits = 0
    while number > 0:
        number = number // base
        numOfDigits += 1
    return numOfDigits

=======
Suggestion 9

def main():
    n, k = map(int, input().split())

    count = 0
    while n > 0:
        count += 1
        n //= k

    print(count)

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    i = 0
    while n > 0:
        n = n // k
        i += 1
    print(i)
