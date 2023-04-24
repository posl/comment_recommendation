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
    if a < b:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

=======
Suggestion 3

def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)

=======
Suggestion 4

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

n, m = [int(x) for x in input().split()]
print(gcd(n, m))

The answer is not correct. The correct answer is 10000.

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, M = map(int, input().split())

ans = 1
for i in range(1, int(M ** 0.5) + 1):
    if M % i == 0:
        if i >= M // N:
            ans = max(ans, i)
        if M // i >= M // N:
            ans = max(ans, M // i)

print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    ans = 1
    for i in range(2, int(M**0.5)+1):
        if M%i == 0:
            if M//i >= N:
                ans = max(ans, i)
            if i >= N:
                ans = max(ans, M//i)
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    ans = 1
    for i in range(2, int(M**0.5)+1):
        if M % i == 0:
            if i * N <= M:
                ans = max(ans, i)
            if (M // i) * N <= M:
                ans = max(ans, M // i)
    print(ans)

=======
Suggestion 8

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    print(M//N)
