Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def count_divisors(n):
    if n == 1:
        return 1
    count = 2
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 2

def count_divisors(n):
    # 1 is always a divisor
    count = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count

=======
Suggestion 3

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, n, 2):
            if n % i == 0:
                return False
        return True

=======
Suggestion 4

def get_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 5

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 6

def count_divisors(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    return count

=======
Suggestion 7

def countDivisors(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count += 1
    return count

=======
Suggestion 8

def solve(n):
    cnt = 0
    for i in range(1,n+1,2):
        div = 0
        for j in range(1,i+1):
            if i%j == 0:
                div += 1
        if div == 8:
            cnt += 1
    return cnt

=======
Suggestion 9

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
