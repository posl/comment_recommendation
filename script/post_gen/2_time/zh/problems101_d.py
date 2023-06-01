Synthesizing 10/10 solutions

=======
Suggestion 1

def calcS(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 2

def S(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

K=int(input())
n=0
while K>0:
    n+=1
    if n%S(n)==0:
        K-=1
print(n)

=======
Suggestion 3

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

=======
Suggestion 4

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 5

def s(n):
    return sum(map(int, str(n)))

k = int(input())
n = 1
while k > 0:
    if s(n) * n >= n:
        print(n)
        k -= 1
    n += 1

=======
Suggestion 6

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

K = int(input())
n = 0
while K > 0:
    n += 1
    if n % S(n) == 0:
        K -= 1
print(n)

=======
Suggestion 7

def S(n):
    n = str(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    return sum

=======
Suggestion 8

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 9

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 10

def S(n):
    sum = 0
    while n>0:
        sum += n%10
        n = n//10
    return sum

k = int(input())
count = 0
n = 1
while True:
    if S(n) == 1:
        n += 9
        continue
    if n%S(n) == 0:
        count += 1
        print(n)
    if count == k:
        break
    n += 1
