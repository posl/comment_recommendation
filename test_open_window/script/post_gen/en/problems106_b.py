Synthesizing 10/10 solutions

=======

def countDivisors(n):
    count = 0
    i = 1
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

N = int(input())
count = 0
for i in range(1, N + 1, 2):
    if countDivisors(i) == 8:
        count += 1

print(count)

=======

def countDivisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

=======

def divisors(n):
    i = 1
    count = 0
    while i * i <= n:
        if n % i == 0:
            if n / i == i:
                count = count + 1
            else:
                count = count + 2
        i = i + 1
    return count

=======

def getDivisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======

def findDivisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

=======

def divisors(n):
    divs = 0
    for i in range(1,n+1):
        if n % i == 0:
            divs += 1
    return divs

=======

def getDivisors(n):
    divisors = []
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

N = int(input())
count = 0
for i in range(1,N+1):
    if len(getDivisors(i)) == 8:
        count += 1
print(count)

=======

def factor_count(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

N = int(input())

count = 0
for i in range(1, N+1):
    if i % 2 != 0 and factor_count(i) == 8:
        count += 1

print(count)

I think my code is too long. How can I make it short?

I tried to use list comprehension, but I couldn't.

=======

def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

=======

def numDivisors(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count
