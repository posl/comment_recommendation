Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

=======
Suggestion 2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    ans = 1
    for i in range(1, int(m ** 0.5) + 1):
        if m % i == 0:
            if i >= m // n:
                ans = max(ans, i)
            if m // i >= m // n:
                ans = max(ans, m // i)
    print(ans)

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N, M = map(int, input().split())

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    ans = 1
    for i in range(1, int(M**0.5)+1):
        if M % i == 0:
            if M // i >= N:
                ans = max(ans, i)
            if i >= N:
                ans = max(ans, M // i)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    print(M // N)
