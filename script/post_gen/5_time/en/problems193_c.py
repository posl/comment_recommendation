Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = set()
    for i in range(2, int(n**0.5) + 1):
        x = i * i
        while x <= n:
            s.add(x)
            x *= i
    print(n - len(s))

=======
Suggestion 2

def main():
    n = int(input())
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        j = 2
        while i ** j <= n:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    ans = N
    for i in range(2, int(N**0.5)+1):
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 4

def solve():
    N = int(input())
    ans = N
    for i in range(2, int(N**0.5)+1):
        j = 2
        while i**j <= N:
            ans -= 1
            j += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    a = 2
    b = 2
    s = set()
    while a**b <= n:
        while a**b <= n:
            s.add(a**b)
            b += 1
        a += 1
        b = 2
    print(n - len(s))

=======
Suggestion 6

def main():
    n = int(input())
    ans = n
    for i in range(2, int(n ** 0.5) + 1):
        num = i * i
        while num <= n:
            ans -= 1
            num *= i
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = set()
    for i in range(2, int(N**0.5)+1):
        x = i*i
        while x <= N:
            ans.add(x)
            x *= i
    print(N-len(ans))

=======
Suggestion 8

def main():
    N = int(input())
    ans = N
    for a in range(2, int(N**0.5)+1):
        x = a*a
        while x <= N:
            ans -= 1
            x *= a
    print(ans)

=======
Suggestion 9

def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n**0.5)+1, 2):
        while n % i== 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(n)
    return factors

=======
Suggestion 10

def get_input():
    n = int(input())
    return n
