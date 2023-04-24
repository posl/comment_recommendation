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

n = int(input())
ans = 0
for i in set(prime_factorize(n)):
    j = 1
    while n % (i ** j) == 0:
        n //= (i ** j)
        j += 1
    ans += j - 1
print(ans)

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

n = int(input())
factors = prime_factorize(n)

=======
Suggestion 3

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

n=int(input())
a=prime_factorize(n)
b=set(a)
c=[]
for i in b:
  c.append(a.count(i))
ans=0
for i in c:
  j=1
  while i>=j:
    i-=j
    j+=1
    ans+=1
print(ans)

=======
Suggestion 4

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

n=int(input())
a=prime_factorize(n)
b=[]
for i in a:
    if i not in b:
        b.append(i)
c=[]
for i in b:
    j=0
    while i**j<=n:
        j+=1
    c.append(j-1)
print(sum(c))

=======
Suggestion 5

def factorize(n):
    fct = []
    b, e = 2, 0
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct

n = int(input())
factors = factorize(n)
ans = 0
for _, e in factors:
    i = 1
    while e >= i:
        e -= i
        i += 1
        ans += 1
print(ans)

=======
Suggestion 6

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct

n = int(input())
fct = factorize(n)
print(len(set(fct)))

=======
Suggestion 7

def prime_factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i == 0:
            cnt = 0
            while temp%i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n, 1])
    return arr

=======
Suggestion 8

def main():
    N = int(input())
    ans = 0
    for i in range(2, int(N**0.5)+1):
        while N % i == 0:
            N //= i
            ans += 1
    if N > 1:
        ans += 1
    print(ans)

=======
Suggestion 9

def getPrimeFactors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n / i
        i = i + 2
    if n > 2:
        factors.append(n)
    return factors

N = int(input())

primeFactors = getPrimeFactors(N)
primeFactors.sort()

count = 1
prev = primeFactors[0]
for i in range(1, len(primeFactors)):
    if primeFactors[i] != prev:
        count += 1
        prev = primeFactors[i]

print(count)

=======
Suggestion 10

def main():
    n = int(input())
    primes = [2]
    for i in range(3, int(n**0.5)+1, 2):
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
    count = 0
    for i in primes:
        while n % i == 0:
            n //= i
            count += 1
    if n != 1:
        count += 1
    print(count)
