Synthesizing 10/10 solutions

=======
Suggestion 1

def f(n):
    ans=0
    for i in range(1,n+1):
        if n%i==0:
            ans+=1
    return ans

n=int(input())
ans=0
for i in range(1,n+1):
    ans+=i*f(i)
print(ans)

=======
Suggestion 2

def f(x):
    ret = 0
    for i in range(1, x+1):
        if x % i == 0:
            ret += 1
    return ret

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 3

def f(x):
    i = 1
    sum = 0
    while i * i <= x:
        if x % i == 0:
            sum += i
            if i * i != x:
                sum += x / i
        i += 1
    return sum - x

n = int(raw_input())
sum = 0
for i in range(1, n + 1):
    sum += i * f(i)
print sum

=======
Suggestion 4

def f(x):
    sum = 0
    for i in range(1,x+1):
        if x%i == 0:
            sum += 1
    return sum

=======
Suggestion 5

def f(x):
    result = 0
    for i in range(1, x+1):
        if x % i == 0:
            result += 1
    return result

n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i * f(i)

print(sum)

=======
Suggestion 6

def f(x):
    sum = 0
    for i in range(1,x+1):
        if x % i == 0:
            sum += 1
    return sum

n = int(input())
sum = 0
for i in range(1,n+1):
    sum += i * f(i)
print(sum)

=======
Suggestion 7

def f(x):
    return sum([1 for k in range(1, x+1) if x % k == 0])

=======
Suggestion 8

def f(x):
    #xの正除数の和を求める
    return sum([i for i in range(1,x+1) if x%i==0])

=======
Suggestion 9

def f(x):
    res = 0
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            res += i
            if i != x // i:
                res += x // i
    return res

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 10

def f(x):
    result = 0
    for i in range(1, x+1):
        if x % i == 0:
            result += 1
    return result
