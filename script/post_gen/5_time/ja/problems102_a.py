Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    print(2*N)

=======
Suggestion 2

def main():
    n = int(input())
    print(n*2)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def main():
    n = int(input())
    ans = 0
    for i in range(1, 10**9):
        if i % 2 == 0 and i % n == 0:
            ans = i
            break
    print(ans)

=======
Suggestion 5

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
print(n * 2 // gcd(n, 2))

=======
Suggestion 6

def main():
    N = int(input())
    if N % 2 == 0:
        print(N)
    else:
        print(N * 2)

=======
Suggestion 7

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N = int(input())
print(N * 2 // gcd(2, N))

=======
Suggestion 8

def solve():
    n = int(input())
    if n % 2 == 0:
        print(n)
    else:
        print(n * 2)

=======
Suggestion 9

def lcm(a,b):
    return a*b // gcd(a,b)
