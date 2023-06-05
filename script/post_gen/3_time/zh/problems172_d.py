Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    r = 0
    for i in range(1, x + 1):
        if x % i == 0:
            r += 1
    return r

=======
Suggestion 2

def f(x):
    s = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            s += i
            if i != x / i:
                s += x / i
    return s

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 3

def f(x):
    #return sum([1 for i in range(1,x+1) if x%i==0])
    #return sum([1 for i in range(1,x+1) if x%i==0])
    return len([i for i in range(1,x+1) if x%i==0])

N = int(input())
print(sum([i*f(i) for i in range(1,N+1)]))

=======
Suggestion 4

def f(x):
    sum = 0
    for i in range(1,x):
        if x % i == 0:
            sum += i
    return sum

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i * f(i)
print(sum)

=======
Suggestion 5

def f(x):
    ret = 0
    for i in range(1, x+1):
        if x % i == 0:
            ret += 1
    return ret

=======
Suggestion 6

def get_divisor_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * f(i)
    return sum

=======
Suggestion 7

def f(x):
    ans = 0
    for i in range(1, x+1):
        if x % i == 0:
            ans += 1
    return ans

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 8

def f(x):
    return sum([i for i in range(1, x + 1) if x % i == 0])

n = int(input())
print(sum([i * f(i) for i in range(1, n + 1)]))

=======
Suggestion 9

def f(x):
    res = 0
    for i in range(1, x+1):
        if x % i == 0:
            res += 1
    return res
