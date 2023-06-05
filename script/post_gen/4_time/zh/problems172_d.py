Synthesizing 10/10 solutions

=======
Suggestion 1

def divisors(x):
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors

=======
Suggestion 2

def f(x):
    s = 0
    for i in range(1, x+1):
        if x % i == 0:
            s += 1
    return s

n = int(input())
s = 0
for i in range(1, n+1):
    s += i * f(i)
print(s)

=======
Suggestion 3

def f(x):
    return sum([i for i in range(1,x+1) if x%i==0])

=======
Suggestion 4

def f(x):
    ans = 0
    i = 1
    while i*i <= x:
        if x % i == 0:
            ans += i
            if i != x // i:
                ans += x // i
        i += 1
    return ans

n = int(input())
ans = 0
for k in range(1, n+1):
    ans += k * f(k)
print(ans)

=======
Suggestion 5

def f(x):
    sum = 0
    for i in range(1,x+1):
        if x%i == 0:
            sum += i
    return sum

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i*f(i)
print(sum)

=======
Suggestion 6

def f(x):
    ans = 0
    for i in range(1, x+1):
        if x % i == 0:
            ans += 1
    return ans

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i * f(i)
    print(ans)

=======
Suggestion 8

def f(x):
    sum = 0
    for i in range(1,x+1):
        if x % i == 0:
            sum += 1
    return sum

=======
Suggestion 9

def f(x):
    return sum([i for i in range(1, x+1) if x % i == 0])

n = int(input())
print(sum([i * f(i) for i in range(1, n+1)]))

=======
Suggestion 10

def f(x):
    res = 0
    for i in range(1, x + 1):
        if x % i == 0:
            res += 1
    return res
