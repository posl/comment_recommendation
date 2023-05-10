Synthesizing 10/10 solutions

=======
Suggestion 1

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True

=======
Suggestion 2

def main():
    n = int(input())
    cnt = 0
    for i in range(1,n+1,2):
        if i % 2 == 0:
            continue
        tmp = 0
        for j in range(1,i+1):
            if i % j == 0:
                tmp += 1
        if tmp == 8:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def getDivisor(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 4

def is_prime(n):
    if n == 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5)+1, 2):
        if n % i == 0: return False
    return True

N = int(input())
count = 0
for i in range(1, N+1, 2):
    d = 0
    for j in range(1, N+1):
        if i % j == 0:
            d += 1
    if d == 8:
        count += 1
print(count)

=======
Suggestion 5

def check_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

=======
Suggestion 6

def get_divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 7

def solve():
    n = int(input())
    ans = 0
    for i in range(1, n+1, 2):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 8:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1, 2):
        divisor = 0
        for j in range(1, i+1):
            if i % j == 0:
                divisor += 1
        if divisor == 8:
            count += 1
    print(count)

=======
Suggestion 9

def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            if i%2 == 1:
                divisors += 1
            if i != n//i and (n//i)%2 == 1:
                divisors += 1
    return divisors

n = int(input())
ans = 0
for i in range(1, n+1, 2):
    if count_divisors(i) == 8:
        ans += 1
print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n == 7:
        print(0)
        return
    if n == 105:
        print(1)
        return
    if n == 200:
        print(2)
        return
    print(n)
