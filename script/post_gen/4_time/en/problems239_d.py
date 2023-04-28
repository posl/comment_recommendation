Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B, C, D = map(int, input().split())
    for i in range(A, B+1):
        for j in range(C, D+1):
            if (i + j) % 2 == 0:
                print("Takahashi")
                return
    print("Aoki")

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
    return True

A, B, C, D = map(int, input().split())

for i in range(B, A-1, -1):
    if is_prime(i):
        first = i
        break
for i in range(C, D+1):
    if is_prime(i):
        second = i
        break

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

a, b, c, d = map(int, input().split())

=======
Suggestion 4

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

a, b, c, d = list(map(int, input().split()))

for i in range(100):
    if a + i <= b and c + i <= d:
        if is_prime(a + i + c + i):
            print("Aoki")
            break
    else:
        print("Takahashi")
        break

=======
Suggestion 5

def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False

    i = 3
    while i <= x ** 0.5:
        if x % i == 0:
            return False
        i += 2

    return True

a, b, c, d = map(int, input().split())

for i in range(b, d+1):
    if is_prime(i) == True:
        print("Aoki")
        exit()

print("Takahashi")

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())
Takahashi = 0
Aoki = 0

for i in range(A, B+1):
    if is_prime(i):
        Takahashi += 1

for i in range(C, D+1):
    if is_prime(i):
        Aoki += 1

=======
Suggestion 7

def isPrime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, n, 2):
        if n%i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())
for i in range(A, B+1):
    for j in range(C, D+1):
        if isPrime(i+j):
            print("Takahashi")
            exit()
print("Aoki")

=======
Suggestion 8

def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

a, b, c, d = map(int, input().split())

for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            print("Takahashi")
            exit()
print("Aoki")

=======
Suggestion 9

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                return False
    return True

a, b, c, d = map(int, input().split())
takahashi = False
for i in range(a, b+1):
    for j in range(c, d+1):
        if is_prime(i+j):
            takahashi = True
            break

=======
Suggestion 10

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1): # i*i <= n
        if n % i == 0:
            return False
    return True

A, B, C, D = map(int, input().split())

for i in range(1, 100):
    if A <= A+i <= B and C <= A+i <= D and isPrime(A+i):
        print("Aoki")
        break
    elif A <= B-i <= B and C <= B-i <= D and isPrime(B-i):
        print("Aoki")
        break
    elif A <= C+i <= B and C <= C+i <= D and isPrime(C+i):
        print("Aoki")
        break
    elif A <= D-i <= B and C <= D-i <= D and isPrime(D-i):
        print("Aoki")
        break
    elif A+i > B:
        print("Takahashi")
        break
    elif B-i < A:
        print("Takahashi")
        break
    elif C+i > D:
        print("Takahashi")
        break
    elif D-i < C:
        print("Takahashi")
        break
