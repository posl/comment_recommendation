Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count

n = int(input())
sum = 0
for i in range(1, n + 1):
    sum += i * f(i)
print(sum)

=======
Suggestion 2

def f(x):
    count=0
    for i in range(1,x+1):
        if x%i==0:
            count+=1
    return count

n=int(input())
ans=0
for i in range(1,n+1):
    ans+=i*f(i)
print(ans)

=======
Suggestion 3

def f(x):
    ret = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            ret += 1
            if i != x // i:
                ret += 1
    return ret

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 4

def f(x):
    n = 0
    for i in range(1, x+1):
        if x % i == 0:
            n += 1
    return n

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 5

def divisor(n):
    cnt = 0
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            cnt += 1
            if i != n // i:
                cnt += 1
    return cnt

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += divisor(i) * i
print(ans)

=======
Suggestion 6

def f(x):
    if x == 1:
        return 1
    else:
        count = 2
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                if i == x / i:
                    count += 1
                else:
                    count += 2
        return count

n = int(input())
ans = 0
for i in range(n):
    ans += (i + 1) * f(i + 1)
print(ans)

=======
Suggestion 7

def f(x):
    if x == 1:
        return 1
    else:
        count = 0
        for i in range(1, int(x**0.5)+1):
            if x % i == 0:
                count += 2
        if int(x**0.5) == x**0.5:
            count -= 1
        return count

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 8

def f(x):
    counter = 0
    for i in range(1, x+1):
        if x % i == 0:
            counter += 1
    return counter

n = int(input())

sum = 0
for i in range(1, n+1):
    sum += i * f(i)
print(sum)

=======
Suggestion 9

def f(x):
    divisors = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            divisors += 2
    return divisors

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i * f(i)
print(ans)
