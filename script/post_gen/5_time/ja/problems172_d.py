Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x):
    ans = 0
    for i in range(1, x + 1):
        if x % i == 0:
            ans += 1
    return ans

N = int(input())
ans = 0
for i in range(1, N + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 2

def f(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 3

def f(x):
    if x == 1:
        return 1
    else:
        i = 2
        count = 2
        while i * i <= x:
            if i * i == x:
                count += 1
            elif x % i == 0:
                count += 2
            i += 1
        return count

n = int(input())
ans = 0
for i in range(1, n + 1):
    ans += i * f(i)
print(ans)

=======
Suggestion 4

def solve(n):
    ans = 0
    for i in range(1, n+1):
        ans += i * f(i)
    return ans

=======
Suggestion 5

def f(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt

N = int(input())
ans = 0
for i in range(1, N+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 6

def divisors(n):
    divisors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    return divisors

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * len(divisors(i))
print(ans)

=======
Suggestion 7

def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num//i)
    return divisors


n = int(input())

ans = 0
for i in range(1, n+1):
    divisors = get_divisors(i)
    ans += i * len(divisors)

print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        #print("i", i)
        for j in range(1, i+1):
            #print("j", j)
            if i % j == 0:
                ans += i
    print(ans)

=======
Suggestion 9

def f(x):
    cnt = 0
    for i in range(1,x+1):
        if x % i == 0:
            cnt += 1
    return cnt

n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i * f(i)
print(ans)
