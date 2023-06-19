Synthesizing 10/10 solutions

=======
Suggestion 1

def count_divisors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 2

def get_divisor_count(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

=======
Suggestion 3

def main():
    N = int(input())
    count = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            continue
        else:
            factor_list = []
            for j in range(1, i + 1):
                if i % j == 0:
                    factor_list.append(j)
            if len(factor_list) == 8:
                count += 1
    print(count)

=======
Suggestion 4

def countDivisors(num):
    count = 0
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            count += 2
    return count

=======
Suggestion 5

def get_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 6

def isprime(n):
    if n == 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

=======
Suggestion 7

def get_divisor_count(n):
    count = 0
    for i in range(1, int(n**0.5+1)):
        if n % i == 0:
            count += 2
    if int(n**0.5)**2 == n:
        count -= 1
    return count

=======
Suggestion 8

def get_divisors(n):
    divisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisors += 1
    return divisors

=======
Suggestion 9

def divisors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return count

=======
Suggestion 10

def get_divisor(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res
