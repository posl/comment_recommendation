Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def getSum(n):
    s = 0
    while n > 0:
        s += n%10
        n = n//10
    return s

=======
Suggestion 2

def s(n):
    return sum(map(int, str(n)))

K = int(input())
ans = []
i = 1
while len(ans) < K:
    if i % s(i) == 0:
        ans.append(i)
    i += 1
for i in ans:
    print(i)

=======
Suggestion 3

def S(n):
    m = str(n)
    sum = 0
    for i in range(len(m)):
        sum = sum + int(m[i])
    return sum

K = int(input())
n = 1
while K > 0:
    if S(n) * n <= S(n+1) * (n+1):
        print(n)
        K = K - 1
    n = n + 1

=======
Suggestion 4

def S(n):
    return sum([int(i) for i in str(n)])

=======
Suggestion 5

def s(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

=======
Suggestion 6

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

K = int(input())
n = 1
while K > 0:
    if n % S(n) == 0:
        print(n)
        K -= 1
    n += 1

=======
Suggestion 7

def S(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

=======
Suggestion 8

def S(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum

K = int(input())
i = 0
n = 1
while i < K:
    if n % S(n) == 0:
        print(n)
        i += 1
    n += 1

=======
Suggestion 9

def S(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

k = int(input())
n = 1
while k > 0:
    if S(n) == 1:
        print(n)
        k -= 1
    n += 1
