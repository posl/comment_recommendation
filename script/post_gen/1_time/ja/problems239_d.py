Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())
ans = "Aoki"
for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            ans = "Takahashi"
            break
    if ans == "Takahashi":
        break
print(ans)

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

a, b, c, d = map(int, input().split())

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

A, B, C, D = map(int, input().split())
ans = "Aoki"
for i in range(C, D+1):
    for j in range(A, B+1):
        if is_prime(i+j):
            ans = "Takahashi"
            break
    if ans == "Takahashi":
        break
print(ans)

=======
Suggestion 4

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

A, B, C, D = map(int, input().split())

=======
Suggestion 5

def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 6

def isPrime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

=======
Suggestion 7

def prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

A, B, C, D = map(int, input().split())

=======
Suggestion 8

def prime_list(n):
    prime = [2]
    for i in range(3, n + 1, 2):
        for p in prime:
            if i % p == 0:
                break
        else:
            prime.append(i)
    return prime

=======
Suggestion 9

def takahashi(A, B, C, D):
    if (A <= 2 and B >= 2) or (C <= 2 and D >= 2):
        return "Aoki"
    else:
        return "Takahashi"

A, B, C, D = map(int, input().split())
print(takahashi(A, B, C, D))
