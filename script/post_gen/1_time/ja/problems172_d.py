Synthesizing 8/10 solutions

=======
Suggestion 1

def divisor(n):
    i = 1
    table = []
    while i*i <= n:
        if n%i == 0:
            table.append(i)
            if i != n//i:
                table.append(n//i)
        i += 1
    return table

N = int(input())
ans = 0
for i in range(1,N+1):
    ans += i*len(divisor(i))
print(ans)

=======
Suggestion 2

def f(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 3

def f(x):
    count = 0
    for i in range(1,x+1):
        if x % i == 0:
            count += 1
    return count

n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i * f(i)
print(ans)

=======
Suggestion 4

def f(x):
    i = 1
    count = 0
    while i*i <= x:
        if x % i == 0:
            count += 2
        if i*i == x:
            count -= 1
        i += 1
    return count

n = int(input())
ans = 0
for i in range(1, n+1):
    ans += i*f(i)
print(ans)

=======
Suggestion 5

def f(x):
    i = 1
    cnt = 0
    while i*i <= x:
        if x%i == 0:
            cnt += 1
            if i*i != x:
                cnt += 1
        i += 1
    return cnt

n = int(input())
ans = 0
for i in range(1,n+1):
    ans += i*f(i)
print(ans)

=======
Suggestion 6

def divisor(x):
    i = 1
    result = 0
    while i*i <= x:
        if x%i == 0:
            result += 1
            if x//i != i:
                result += 1
        i += 1
    return result

n = int(input())

ans = 0
for i in range(1, n+1):
    ans += i*divisor(i)
print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    ans = 0
    for i in range(1,N+1):
        ans += i * f(i)
    print(ans)

=======
Suggestion 8

def get_divisor_list(x):
    divisor_list = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            divisor_list.append(i)
            if i != x // i:
                divisor_list.append(x // i)
        i += 1
    return divisor_list

N = int(input())

ans = 0
for i in range(1, N + 1):
    ans += i * len(get_divisor_list(i))
print(ans)
