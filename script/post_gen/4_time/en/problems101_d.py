Synthesizing 10/10 solutions

=======
Suggestion 1

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 2

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 3

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

k = int(input())
n = 1
while k > 0:
    if n / S(n) <= (n + 1) / S(n + 1):
        print(n)
        k -= 1
    n += 1

=======
Suggestion 4

def S(n):
    if n < 10:
        return n
    else:
        return n%10 + S(n//10)

=======
Suggestion 5

def S(n):
    return sum(int(i) for i in str(n))

K = int(input())
ans = []
n = 1
while len(ans) < K:
    if n / S(n) <= (n+1) / S(n+1):
        ans.append(n)
    n += 1
for i in ans:
    print(i)

=======
Suggestion 6

def S(n):
    return sum(int(i) for i in str(n))

K = int(input())

n = 1
ans = []

while len(ans) < K:
    if n / S(n) <= (n+1) / S(n+1):
        ans.append(n)
    n += 1

print(*ans, sep='\n')

=======
Suggestion 7

def S(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 8

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

=======
Suggestion 9

def sum_digits(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 10

def S(n):
    return sum(map(int, str(n)))
