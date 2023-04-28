Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 2

def f(x):
    divisors = 0
    for i in range(1, x+1):
        if x % i == 0:
            divisors += 1
    return divisors

=======
Suggestion 3

def f(x):
    divisors = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisors += 1
            if x // i != i:
                divisors += 1
    return divisors

n = int(input())

ans = 0
for k in range(1, n+1):
    ans += k * f(k)

print(ans)

=======
Suggestion 4

def f(x):
    return len([i for i in range(1, x+1) if x % i == 0])

n = int(input())
print(sum([i * f(i) for i in range(1, n+1)]))

=======
Suggestion 5

def f(n):
    count = 0
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count

N = int(input())
result = 0
for i in range(1,N+1):
    result += i * f(i)
print(result)

=======
Suggestion 6

def f(x):
    res = 0
    for i in range(1, int(x**0.5)+1):
        if x%i == 0:
            res += 2
            if i == x**0.5:
                res -= 1
    return res

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i*f(i)
print(ans)

=======
Suggestion 7

def f(x):
    divisor = 0
    for i in range(1,x+1):
        if x % i == 0:
            divisor += 1
    return divisor

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i * f(i)
print(sum)

=======
Suggestion 8

def f(x):
    r = 0
    for i in range(1, int(x**.5)+1):
        if x % i == 0:
            r += 1
            if i != x // i:
                r += 1
    return r

n = int(input())
r = 0
for i in range(1, n+1):
    r += i * f(i)
print(r)

=======
Suggestion 9

def f(x):
    divs = 0
    for i in range(1, x+1):
        if x%i == 0:
            divs += 1
    return divs

n = int(input())

total = 0
for i in range(1, n+1):
    total += i*f(i)

print(total)

=======
Suggestion 10

def get_divisors(x):
    divisors = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisors += 1
            if x // i != i:
                divisors += 1
    return divisors

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * get_divisors(i)
print(ans)
