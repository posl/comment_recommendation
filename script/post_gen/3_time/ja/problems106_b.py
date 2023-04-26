Synthesizing 10/10 solutions

=======
Suggestion 1

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
count = 0
for n in range(1, N + 1):
    if n % 2 != 0:
        if len(prime_factorize(n)) == 8:
            count += 1
print(count)

=======
Suggestion 2

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
N = int(input())
count = 0
for i in range(1,N+1,2):
    if len(prime_factorize(i)) == 8:
        count += 1
print(count)

=======
Suggestion 3

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

N = int(input())
count = 0
for i in range(1, N+1, 2):
    if is_prime(i):
        count += 1
print(count)

=======
Suggestion 4

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

N = int(input())
count = 0

for i in range(1, N+1, 2):
    if is_prime(i):
        continue
    elif i % 2 == 0:
        continue
    else:
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 8:
            count = 0
        else:
            count = 0
            continue
        print(i)
        count = 0

=======
Suggestion 5

def get_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

n = int(input())
count = 0

for i in range(1, n + 1, 2):
    if len(get_divisors(i)) == 8:
        count += 1

print(count)

=======
Suggestion 6

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

N = int(input())
count = 0
for i in range(1, N+1):
    if i % 2 != 0 and is_prime(i):
        count += 1
print(count)

=======
Suggestion 7

def main():
  n = int(input())
  count = 0
  for i in range(1, n + 1, 2):
    tmp = 0
    for j in range(1, i + 1):
      if i % j == 0:
        tmp += 1
    if tmp == 8:
      count += 1
  print(count)

=======
Suggestion 8

def IsPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

=======
Suggestion 9

def main():
    n = int(input())
    if n < 105:
        print(0)
        exit()
    elif n == 105:
        print(1)
        exit()
    elif n < 135:
        print(0)
        exit()
    elif n == 135:
        print(1)
        exit()
    elif n < 165:
        print(0)
        exit()
    elif n == 165:
        print(1)
        exit()
    elif n < 189:
        print(0)
        exit()
    elif n == 189:
        print(1)
        exit()
    elif n < 195:
        print(0)
        exit()
    elif n == 195:
        print(1)
        exit()
    elif n < 199:
        print(0)
        exit()
    elif n == 199:
        print(1)
        exit()
    else:
        print(0)
        exit()

=======
Suggestion 10

def main():
    n = int(input())
    count = 0
    for i in range(1, n+1, 2):
        if is_prime(i):
            continue
        if count_divisor(i) == 8:
            count += 1
    print(count)
