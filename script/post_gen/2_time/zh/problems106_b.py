Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

=======
Suggestion 2

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 3

def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

=======
Suggestion 4

def count_dividers(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

n = int(input())
count = 0
for i in range(1, n+1, 2):
    if count_dividers(i) == 8:
        count += 1
print(count)

=======
Suggestion 5

def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
        return True

=======
Suggestion 6

def find_divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 7

def isPrime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    if num == 1:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

=======
Suggestion 8

def get_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 9

def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

N = int(input())
count = 0
for i in range(1, N + 1, 2):
    if len(get_divisors(i)) == 8:
        count += 1
print(count)

=======
Suggestion 10

def is_prime(n):
    if n % 2 == 0 and n != 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True
