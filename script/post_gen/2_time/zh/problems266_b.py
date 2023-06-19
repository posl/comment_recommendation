Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print((998244353 - n % 998244353) % 998244353)

=======
Suggestion 2

def main():
    N = int(input())
    print(N%998244353)

=======
Suggestion 3

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 4

def b(N):
    return (998244353-(N%998244353))%998244353

=======
Suggestion 5

def solve(n):
    return (998244353 - (n % 998244353)) % 998244353

=======
Suggestion 6

def main():
    n = int(input())
    print((-n)%998244353)

=======
Suggestion 7

def main():
    n = int(input())

    if n < 0:
        n = -n
        n = n % 998244353
        n = 998244353 - n
    else:
        n = n % 998244353

    print(n)

=======
Suggestion 8

def main():
    N = int(input())
    print((998244353 - N % 998244353) % 998244353)
