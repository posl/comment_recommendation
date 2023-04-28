Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    return cnt

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 2

def f(x):
    count = 0
    for i in range(1,x+1):
        if x % i == 0:
            count += 1
    return count

N = int(input())
ans = 0
for i in range(1,N+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 3

def f(x):
    i = 1
    count = 0
    while i * i <= x:
        if x % i == 0:
            count += 1
            if x // i != i:
                count += 1
        i += 1
    return count

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 4

def f(x):
    count = 0
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            count += 1
            if i != x//i:
                count += 1
    return count

n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i*f(i)
print(ans)

=======
Suggestion 5

def f(n):
    ans = 0
    for i in range(1,n+1):
        if n%i == 0:
            ans += 1
    return ans

n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i*f(i)
print(ans)

=======
Suggestion 6

def f(x):
    r = 0
    for i in range(1, x+1):
        if x % i == 0:
            r += 1
    return r

n = int(input())
r = 0
for i in range(1, n+1):
    r += i * f(i)
print(r)

=======
Suggestion 7

def f(n):
    ret = 0
    i = 1
    while i*i <= n:
        if n%i == 0:
            ret += 1
            if i != n//i:
                ret += 1
        i += 1
    return ret

n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i*f(i)
print(ans)

=======
Suggestion 8

def f(x):
    if x == 1:
        return 1
    else:
        cnt = 0
        for i in range(1, int(x**0.5)+1):
            if x % i == 0:
                cnt += 2
        if int(x**0.5)**2 == x:
            cnt -= 1
        return cnt

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * len([j for j in range(1, i+1) if i % j == 0])
    print(ans)

=======
Suggestion 10

def get_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: 
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * len(get_divisors(i))
print(ans)
