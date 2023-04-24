Synthesizing 10/10 solutions

=======
Suggestion 1

def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

=======
Suggestion 2

def is_prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    return all(n % i for i in range(3, int(n**0.5)+1, 2))

=======
Suggestion 3

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

=======
Suggestion 4

def findDivisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 5

def divisors(x):
    count = 0
    for i in range(1, x):
        if x % i == 0:
            count += 1
    return count

N = int(input())
count = 0
for i in range(1, N + 1):
    if divisors(i) == 8:
        count += 1
print(count)

=======
Suggestion 6

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        if get_divisor_count(i) == 8:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    count = 0
    for i in range(1, N+1):
        if i % 2 == 0:
            continue
        else:
            if get_divisor(i) == 8:
                count += 1
    print(count)

=======
Suggestion 8

def main():
    n = int(input())
    print(sum(1 for i in range(1, n + 1) if (i % 2) and (len([1 for j in range(1, i + 1) if i % j == 0]) == 8)))

=======
Suggestion 9

def get_divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]

=======
Suggestion 10

def main():
    N = int(input())
    print(N//2)
main()
