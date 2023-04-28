Synthesizing 10/10 solutions

=======
Suggestion 1

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

n = int(input())
count = 0
for i in range(1, n+1):
    if i % 2 == 1 and len(divisors(i)) == 8:
        count += 1
print(count)

=======
Suggestion 2

def is_prime(n):
    if n == 1:
        return False
    else:
        for k in range(2, int(n**0.5)+1):
            if n % k == 0:
                return False
        return True

=======
Suggestion 3

def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 4

def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)
    return divisors

N = int(input())
count = 0

for i in range(1, N+1, 2):
    if len(divisors(i)) == 8:
        count += 1

print(count)

=======
Suggestion 5

def count_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return len(divisors)

n = int(input())
count = 0
for i in range(1, n+1, 2):
    if count_divisors(i) == 8:
        count += 1
print(count)

=======
Suggestion 6

def divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 7

def count_divisors(number):
    divisors = 0
    for i in range(1,number+1):
        if number % i == 0:
            divisors += 1
    return divisors

=======
Suggestion 8

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

=======
Suggestion 9

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if not n % i:
            return False
    return True

n = int(input())
count = 0
for i in range(1, n+1):
    if i % 2 == 1:
        if is_prime(i):
            count += 1
        if count == 8:
            print(i)
            break

=======
Suggestion 10

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
